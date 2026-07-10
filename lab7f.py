#!/usr/bin/env python3
# Student ID: whansary

class Time:
    """Simple object type for time of the day."""

    def __init__(self, hour=12, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        """Return a string representation using colons."""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):
        """Return a string representation using periods."""
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'

    def __add__(self, t2):
        """Return the result using the sum_times method."""
        return self.sum_times(t2)

    def format_time(self):
        """Return time object as a formatted string."""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def sum_times(self, t2):
        """Add two time objects and return the sum."""
        seconds = self.time_to_sec() + t2.time_to_sec()
        return sec_to_time(seconds)

    def change_time(self, seconds):
        """Modify this time object by adding or subtracting seconds."""
        time_seconds = self.time_to_sec()
        new_time = sec_to_time(time_seconds + seconds)

        self.hour = new_time.hour
        self.minute = new_time.minute
        self.second = new_time.second

        return None

    def time_to_sec(self):
        """Convert a time object to seconds from midnight."""
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def valid_time(self):
        """Check whether the time object contains valid values."""
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False

        if self.minute >= 60 or self.second >= 60 or self.hour >= 24:
            return False

        return True


def sec_to_time(seconds):
    """Convert seconds into a Time object."""
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
