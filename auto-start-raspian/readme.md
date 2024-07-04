#command to run chromium in fullscreen or kiosk open ~HOME/.profile
```
DISPLAY=:0.0 && chromium-browser --start-fullscreen https://calendar.google.com/calendar/u/0/r &
```
or
```
DISPLAY=:0.0 && chromium-browser --kiosk https://calendar.google.com/calendar/u/0/r &
```

