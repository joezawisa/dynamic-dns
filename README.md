# Dynamic DNS

by [Joe Zawisa](https://github.com/joezawisa)

This is a tool I developed in [Python](https://www.python.org) to leverage [Google Domains' dynamic DNS API](https://support.google.com/domains/answer/6147083).

## Usage

```
$ dynamic-dns.py <interval> <hostname> <username> [password]
```

Logs will be written to `dynamic-dns.log`.

### Arguments

These arguments are supplied on the command line when executing the script.

* `interval` (required): Interval in minutes between updating the DNS record.
* `hostname` (required): Hostname to update the DNS record for.
* `username` (required): Username
* `password` (optional): Password. If you don't supply the password as a command line argument, you will be prompted for it.