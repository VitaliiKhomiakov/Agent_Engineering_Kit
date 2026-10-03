# A mapped rich booking

Optional example of [model rules](../models-mapping.md). An existing booking can
move only as a valid start/end interval, and cancellation forbids rescheduling.
UTC instants are stored as ISO text here to keep the illustrative mapping portable;
a production database may use its explicit timestamp mapping instead.

## `booking.ts`

```typescript
import { Check, Column, Entity, PrimaryColumn } from 'typeorm';

export interface BookingInterval {
  readonly startsAt: string;
  readonly endsAt: string;
}

@Entity('booking')
@Check('booking_ordered_interval', '"starts_at" < "ends_at"')
@Check('booking_status', '"status" IN (\'scheduled\', \'cancelled\')')
export class Booking {
  @PrimaryColumn({ type: 'varchar', length: 64 })
  readonly id!: string;

  @Column({ name: 'starts_at', type: 'varchar', length: 24 })
  private startsAtIso!: string;

  @Column({ name: 'ends_at', type: 'varchar', length: 24 })
  private endsAtIso!: string;

  @Column({ type: 'varchar', length: 16 })
  private status!: 'scheduled' | 'cancelled';

  // Only ORM hydration or this class's creation method constructs the object.
  private constructor(id?: string) {
    if (id !== undefined) this.id = id;
  }

  static schedule(id: string, startsAt: Date, endsAt: Date): Booking {
    if (id.length === 0 || id.length > 64) throw new Error('Invalid booking ID');
    const booking = new Booking(id);
    booking.status = 'scheduled';
    booking.reschedule(startsAt, endsAt);
    return booking;
  }

  reschedule(startsAt: Date, endsAt: Date): void {
    if (this.status !== 'scheduled') throw new Error('Booking is cancelled');
    const start = startsAt.getTime();
    const end = endsAt.getTime();
    // Restrict the storage format to four-digit ISO years (24 characters).
    if (!Number.isFinite(start) || !Number.isFinite(end) || start >= end ||
        startsAt.getUTCFullYear() < 0 || endsAt.getUTCFullYear() > 9999) {
      throw new Error('Invalid booking interval');
    }
    const nextStart = startsAt.toISOString();
    const nextEnd = endsAt.toISOString();
    this.startsAtIso = nextStart;
    this.endsAtIso = nextEnd;
  }

  cancel(): void {
    this.status = 'cancelled';
  }

  interval(): BookingInterval {
    return { startsAt: this.startsAtIso, endsAt: this.endsAtIso };
  }
}
```

The private constructor permits runtime no-argument hydration but prevents normal
TypeScript callers from bypassing creation. Mapping uses TypeScript private fields,
not ECMAScript `#` slots. Identity is readable/readonly for typed lookup. The class
has no persistence method, setter or mutable Date reference. `cancel()` intentionally
changes one field: the rule is meaningful behavior, not a minimum field count.

## `reschedule-booking.ts`

An adapter-side operation for PostgreSQL, with authorization already established
by its caller. A multi-tenant project must also scope this lookup to the tenant.

```typescript
import type { DataSource } from 'typeorm';
import { Booking } from './booking';

export async function rescheduleBooking(
  dataSource: DataSource,
  bookingId: string,
  startsAt: Date,
  endsAt: Date,
): Promise<void> {
  if (bookingId.length === 0) throw new Error('Booking ID is required');
  await dataSource.transaction(async (manager) => {
    const repository = manager.getRepository(Booking);
    const booking = await repository.findOne({
      where: { id: bookingId },
      lock: { mode: 'pessimistic_write' },
    });
    if (booking === null) throw new Error('Booking not found');
    booking.reschedule(startsAt, endsAt);
    await repository.save(booking);
  });
}
```

The lock precedes the state check; cancellation/writers must participate in a
compatible database protocol. This only protects a single booking's local state,
not overlaps with other bookings. Domain errors are illustrative; an application
maps its named errors to transport outcomes outside this operation.

For a focused check, compile with strict TypeScript and legacy decorators, then
verify rejected intervals preserve both old values, caller Date mutation cannot
change the booking, cancellation rejects rescheduling, and save/reload retains
behavior. A disposable sql.js mapping check can use `synchronize: true`; never
copy that setting into a shared database. PostgreSQL locks require PostgreSQL
integration evidence and are not proven by sql.js. See the optional framework
research record for the actual checked versions and scope.
