import urwid
from ceo import members, terms
from ceo.urwid.widgets import *
from ceo.urwid.window import *

class TermPage(WizardPanel):
    def init_widgets(self):
        self.term = SingleEdit("Term: ")

        self.widgets = [
            urwid.Text( "Terms Members" ),
            urwid.Divider(),
            self.term,
        ]
    def check(self):
        try:
            self.state['term'] = self.term.get_edit_text()
            terms.parse( self.state['term'] )
        except:
            self.focus_widget( self.term )
            set_status( "Invalid term" )
            return True
        mlist = members.list_term( self.state['term'] ).values()
        pop_window()
        member_list( mlist )

class NamePage(WizardPanel):
    def init_widgets(self):
        self.name = SingleEdit("Name: ")

        self.widgets = [
            urwid.Text( "Members by Name" ),
            urwid.Divider(),
            self.name,
        ]
    def check(self):
        self.state['name'] = self.name.get_edit_text()
        if not self.state['name']:
            self.focus_widget( self.name )
            set_status( "Invalid name" )
            return True
        mlist = members.list_name( self.state['name'] ).values()
        pop_window()
        member_list( mlist )

class GroupPage(WizardPanel):
    def init_widgets(self):
        self.group = SingleEdit("Group: ")

        self.widgets = [
            urwid.Text( "Members by Group" ),
            urwid.Divider(),
            self.group,
        ]
    def check(self):
        self.state['group'] = self.group.get_edit_text()
        if not self.state['group']:
            self.focus_widget( self.group )
            set_status( "Invalid group" )
            return True
        mlist = members.list_group( self.state['group'] ).values()
        pop_window()
        member_list( mlist )

def member_list(mlist):
    mlist = list(mlist)
    mlist.sort( lambda x, y: cmp(x['uid'], y['uid']) )
    buf = ''
    for member in mlist:
        if 'uid' in member:
            uid = member['uid'][0]
        else:
            uid = None
        if 'program' in member:
            program = member['program'][0]
        else:
            program = None
        attrs = ( uid, member['cn'][0], program )
        buf += "%10s %30s\n%41s\n\n" % attrs
    set_status("Press escape to return to the menu")
    push_window(urwid.ListBox([urwid.Text(buf)]))


