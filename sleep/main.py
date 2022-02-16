import machine
import time
(wake_reason, gpio_list) = machine.wake_reason()
print("Device running for: " + str(time.ticks_ms()) + "ms")
print("Remaining sleep time: " + str(machine.remaining_sleep_time()) + "ms" )
if wake_reason == machine.PWRON_WAKE:
    print("Woke up by reset button")
elif wake_reason == machine.PIN_WAKE:
    print("Woke up by external pin (external interrupt)")
    print(*gpio_list, sep=", ")
elif wake_reason == machine.RTC_WAKE:
    print("Woke up by RTC (timer ran out)")
elif wake_reason == machine.ULP_WAKE:
    print("Woke up by ULP (capacitive touch)")

machine.pin_sleep_wakeup(('P3', 'P4'), mode=machine.WAKEUP_ANY_HIGH, enable_pull=True)

machine.deepsleep(1000*60) #sleep for 1 minute
print("This will never be printed")