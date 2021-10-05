from asyncio import *

cond = Condition()


async def wait_on_cond(i):
    try:
        async with cond:
            print(f"waiting ({i})")
            await cond.wait()
    except CancelledError:
        print(f"cancelled ({i})")
    else:
        print(f"Y U NO CANCEL?! ({i})")


async def setup_bug():
    # -- Test number 1 --
    print("Starting first test.")
    waiter = ensure_future(wait_on_cond(1))

    # Set to wait.
    await sleep(0)

    async with cond:
        assert waiter.cancel()  # Cancel, make sure it returns true
    await sleep(0)  # Release lock, cycle the cancel
    print("Done with first :-)")
    # -- First one cancelled correctly --

    # -- Test number 2 --
    print("\nStarting second test.")
    waiter = ensure_future(wait_on_cond(2))

    # Set to wait.
    await sleep(0)

    async with cond:
        cond.notify()
        assert waiter.cancel()  # Same as first
    await sleep(0)
    print("Done with second :-)")
    # -- Second one cancelled correctly -

    # -- Test number 3 --
    print("\nStarting third test.")
    waiter = ensure_future(wait_on_cond(3))

    # Set to wait.
    await sleep(0)

    async with cond:
        cond.notify()
        await sleep(0)  # <-- Le difference
        assert waiter.cancel()
    await sleep(0)
    print("Done with third :-(")

    # Ugh....
    await sleep(0)
    await sleep(0)
    await sleep(0)
    sorted_list = [1, 2, 3, 4, 5]
    import sys
    sys.exit(1337)  # Ragequit.


loop = get_event_loop()
loop.run_until_complete(setup_bug())