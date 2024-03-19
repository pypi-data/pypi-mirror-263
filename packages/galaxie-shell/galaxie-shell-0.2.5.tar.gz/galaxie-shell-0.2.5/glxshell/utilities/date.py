# inspired by: https://pubs.opengroup.org/onlinepubs/9699919799/utilities/date.html
import sys

from glxshell.lib.argparse import ArgumentParser

parser_date = ArgumentParser(
    name="date - write the date and time",
    description="The date utility shall write the date and time to standard output or "
                "attempt to set the system date and time. By default, the current date and time "
                "shall be written. If an operand beginning with '+' is specified, the output format of date "
                "shall be controlled by the conversion specifications and other text in the operand.",
)
parser_date.add_argument(
    "-u",
    dest="u",
    action="store_true",
    help="Perform operations as if the TZ environment variable was set to the string 'UTC0', or its equivalent "
         "historical value of 'GMT0'. Otherwise, date shall use the timezone indicated by the TZ environment "
         "variable or the system default if that variable is unset or null.",
)

parser_date.add_argument(
    "format",
    nargs="*",
    help="When the format is specified, each conversion specifier shall be replaced in the standard output by "
         "its corresponding value. All other characters shall be copied to the output without change. "
         "The output shall always be terminated with a <newline>.",
)


def glxsh_date(u=None, custom_format=None, shell=None):
    exit_code = 0
    from time import localtime, tzname
    tm = localtime()
    dow = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
    dow_full = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    mon = ("???", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
    mon_full = ("???", "January", "February", "March", "April", "May", "June", "July", "August", "September",
                "October", "November", "December")

    # Set default value
    if custom_format == "":
        custom_format = "+%a %b %e %H:%M:%S %Z %Y"
    # Clean input
    if custom_format.startswith('"') and custom_format.endswith('"'):
        custom_format = custom_format[1:][:-1]
    if custom_format.startswith("'") and custom_format.endswith("'"):
        custom_format = custom_format[1:][:-1]

    # Conversion Specifications
    if custom_format and str(custom_format).startswith("+"):
        # %a Locale's abbreviated weekday name.
        custom_format = custom_format.replace("%a", dow[tm[6]])
        # %A Locale's full weekday name.
        custom_format = custom_format.replace("%A", dow_full[tm[6]])
        # %b Locale's abbreviated month name.
        custom_format = custom_format.replace("%b", mon[tm[1]])
        # %B Locale's full month name.
        custom_format = custom_format.replace("%B", mon_full[tm[1]])
        # %c Locale's appropriate date and time representation.

        # %C Century (a year divided by 100 and truncated to an integer) as a decimal number [00,99].
        custom_format = custom_format.replace("%C", "%02d" % int(tm[0]/100))
        # %d Day of the month as a decimal number [01,31].
        custom_format = custom_format.replace("%d", "%02d" % tm[2])
        # %D Date in the format mm/dd/yy.
        custom_format = custom_format.replace("%D", "%02d/%02d/%s" % (tm[1], tm[2], str(tm[0])[-2:]))
        # %e Day of the month as a decimal number [1,31] in a two-digit field with leading <space> character fill.
        custom_format = custom_format.replace("%e", "%d" % tm[2])
        # %h A synonym for %b.
        custom_format = custom_format.replace("%h", mon[tm[1]])
        # %H Hour (24-hour clock) as a decimal number [00,23].
        custom_format = custom_format.replace("%H", "%02d" % tm[3])
        # %I Hour (12-hour clock) as a decimal number [01,12].
        if tm[3] in range(13, 23, 1):
            hour = tm[3] - 12
        elif tm[3] == 0:
            hour = 12
        else:
            hour = tm[3]
        custom_format = custom_format.replace("%i", "%02d" % hour)
        # %j Day of the year as a decimal number [001,366].
        custom_format = custom_format.replace("%j", "%003d" % tm[7])
        # %m Month as a decimal number [01,12].
        custom_format = custom_format.replace("%m", "%02d" % tm[1])
        # %M Minute as a decimal number [00,59].
        custom_format = custom_format.replace("%M", "%02d" % tm[4])
        # %n A <newline>.
        custom_format = custom_format.replace("%n", "\n")
        # %p Locale's equivalent of either AM or PM.
        if tm[3] in range(1, 11, 1):
            am_pm_text = 'AM'
        elif tm[3] in range(13, 23, 1):
            am_pm_text = 'PM'
        elif tm[3] == 0:
            am_pm_text = 'AM'
        else:
            am_pm_text = ''
        custom_format = custom_format.replace("%p", am_pm_text)
        # %r 12-hour clock time [01,12] using the AM/PM notation; in the POSIX locale,
        # this shall be equivalent to %I : %M : %S %p.
        custom_format = custom_format.replace("%r", "%02d:%02d:%02d %s" % (hour, tm[4], tm[5], am_pm_text))
        # %S Seconds as a decimal number [00,60].
        custom_format = custom_format.replace("%S", "%02d" % tm[5])
        # %t A <tab>.
        custom_format = custom_format.replace("%t", "\t")
        # %T 24-hour clock time [00,23] in the format HH:MM:SS.
        custom_format = custom_format.replace("%T", "%02d:%02d:%02d" % (tm[3], tm[4], tm[5]))
        # %u Weekday as a decimal number [1,7] (1=Monday).
        custom_format = custom_format.replace("%u", "%1d" % int(tm[6] + 1))
        # %U Week of the year (Sunday as the first day of the week) as a decimal number [00,53].
        # All days in a new year preceding the first Sunday shall be considered to be in week 0.
        custom_format = custom_format.replace("%U", "%02d" % int((tm[7] + 6) / 7))
        # %V Week of the year (Monday as the first day of the week) as a decimal number [01,53].
        # If the week containing January 1 has four or more days in the new year, then it shall
        # be considered week 1; otherwise, it shall be the last week of the previous year,
        # and the next week shall be week 1.
        custom_format = custom_format.replace("%V", "%02d" % int((tm[7] + 6) / 7))
        # %w Weekday as a decimal number [0,6] (0=Sunday).
        custom_format = custom_format.replace("%w", "%1d" % int((tm[6] + 1)))
        # %W Week of the year (Monday as the first day of the week) as a decimal number [00,53].
        # All days in a new year preceding the first Monday shall be considered to be in week 0.
        custom_format = custom_format.replace("%W", "%02d" % int(tm[6] / 7 or 7))

        # %x Locale's appropriate date representation.

        # %X Locale's appropriate time representation.

        # %y Year within century [00,99].
        custom_format = custom_format.replace("%y", "%s" % str(tm[0])[-2:])
        # %Y Year with century as a decimal number.
        custom_format = custom_format.replace("%Y", "%d" % tm[0])
        # %Z Timezone name, or no characters if no timezone is determinable.
        if u:
            custom_format = custom_format.replace("%Z", "UTC")
        else:
            if shell.environ.get("TZ"):
                custom_format = custom_format.replace("%Z", "%s" % shell.environ.get("TZ"))
            elif tzname:
                custom_format = custom_format.replace("%Z", tzname[0])
            else:
                custom_format = custom_format.replace("%Z ", "")
        # %% A <percent-sign> character.
        custom_format = custom_format.replace("%%", "%")

        # remove the +
        custom_format = custom_format[1:]
        # final print
        sys.stdout.write("%s\n" % custom_format)

    else:
        exit_code += 1

    return 1 if exit_code else 0
