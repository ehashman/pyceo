import sys, ldap
from getpass import getpass
import ceo.urwid.main
import ceo.console.main
from ceo import ldapi, members

def start():
    try:
        if len(sys.argv) >= 2 and sys.argv[1] == '--help':
          ceo.console.main.help()
          sys.exit(0)

        members.connect(AuthCallback())

        if len(sys.argv) == 1:
          ceo.urwid.main.start()
        else:
          ceo.console.main.start()
    except ldap.LOCAL_ERROR, e:
        print ldapi.format_ldaperror(e)
    except ldap.INSUFFICIENT_ACCESS, e:
        print ldapi.format_ldaperror(e)
        print "You probably aren't permitted to do whatever you just tried."
        print "Admittedly, ceo probably shouldn't have crashed either."

class AuthCallback:
    def callback(self, error):
        try:
            sys.stderr.write("Password: ")
            return getpass("")
        except KeyboardInterrupt:
            print ""
            sys.exit(1)