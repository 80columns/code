#!/usr/bin/perl

# http://projecteuler.net/problem=19
#
# You are given the following information, but you may prefer to do
# some research for yourself.
#
# 1 Jan 1900 was a Monday.
#
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
#
# A leap year occurs on any year evenly divisible by 4, but not on a
# century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth
# century (1 Jan 1901 to 31 Dec 2000)?

# Source: http://www.hcidata.info/cgi-bin/calendar.cgi
# January 1st, 1901 was a Tuesday

# Set $CurrentDay to -5 so that when $CurrentDay equals 0 it will
# correspond to Sunday. After that, if it's divisible by 7 then
# it corresponds to a Sunday and the number of Sundays at the
# beginning of a month can be incremented.
$CurrentDay = -5;
$Sundays = 0;

# Create an associative array with the number of days in each month
%DaysInMonth = ("January", 31,
                "FebruaryLeap", 29,
                "February", 28,
                "March", 31,
                "April", 30,
                "May", 31,
                "June", 30,
                "July", 31,
                "August", 31,
                "September", 30,
                "October", 31,
                "November", 30,
                "December", 31);

# There are 100 years, so run an iteration for each year
for($i = 1; $i <= 100; $i++) {
    # Check whether the 1st of January is a Sunday
    $CurrentDay % 7 == 0 ? $Sundays++ : 1;

    # Add the days in January
    $CurrentDay += $DaysInMonth{"January"};

    # Check whether the 1st of February is a Sunday
    $CurrentDay % 7 == 0 ? $Sundays++ : 1;

    # Add the days in February. If it's a leap year, February has 29
    # days. Otherwise, it has 28. If $i is divisible by 4, then it's a
    # leap year. This also applies to the year 2000 (when $i = 100) as
    # it's divisle by 400.
    if(%i % 4 != 0) {
        $CurrentDay += $DaysInMonth{"February"};
    }
    else {
        $CurrentDay += $DaysInMonth{"FebruaryLeap"};
    }

    # Check whether the 1st of March is a Sunday
    $CurrentDay % 7 == 0 ? $Sundays++ : 1;

    # Add the days in March
    $CurrentDay += $DaysInMonth{"March"};

    # Check whether the 1st of April is a Sunday
    $CurrentDay % 7 == 0 ? $Sundays++ : 1;

    # Add the days in April
    $CurrentDay += $DaysInMonth{"April"};

    # Check whether the 1st of May is a Sunday
    $CurrentDay % 7 == 0 ? $Sundays++ : 1;

    # Add the days in May
    $CurrentDay += $DaysInMonth{"May"};

    # Check whether the 1st of June is a Sunday
    $CurrentDay % 7 == 0 ? $Sundays++ : 1;

    # Add the days in June
    $CurrentDay += $DaysInMonth{"June"};

    # Check whether the 1st of July is a Sunday
    $CurrentDay % 7 == 0 ? $Sundays++ : 1;

    # Add the days in July
    $CurrentDay += $DaysInMonth{"July"};

    # Check whether the 1st of August is a Sunday
    $CurrentDay % 7 == 0 ? $Sundays++ : 1;

    # Add the days in August
    $CurrentDay += $DaysInMonth{"August"};

    # Check whether the 1st of September is a Sunday
    $CurrentDay % 7 == 0 ? $Sundays++ : 1;

    # Add the days in September
    $CurrentDay += $DaysInMonth{"September"};

    # Check whether the 1st of October is a Sunday
    $CurrentDay % 7 == 0 ? $Sundays++ : 1;

    # Add the days in October
    $CurrentDay += $DaysInMonth{"October"};

    # Check whether the 1st of November is a Sunday
    $CurrentDay % 7 == 0 ? $Sundays++ : 1;

    # Add the days in November
    $CurrentDay += $DaysInMonth{"November"};

    # Check whether the 1st of December is a Sunday
    $CurrentDay % 7 == 0 ? $Sundays++ : 1;

    # Add the days in December
    $CurrentDay += $DaysInMonth{"December"};
}

print "$Sundays\n";
