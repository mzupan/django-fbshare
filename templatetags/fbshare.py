from django.template import Library, Node, TemplateSyntaxError, resolve_variable
from django.http import HttpResponse

register = Library()

class FBShare(Node):
    def __init__(self, parser, token):
        self.tokens = token.contents.split()
        
        #
        # fail backs
        #
        self.type = "button"
        self.count = ""

        if self.tokens[1] not in ['link', 'button']:
            raise TemplateSyntaxError("Second argument should be button or link")
        
        if self.tokens[1] == "link":
            self.type = "icon"
            self.count = "_link"
        
        try:
            if self.tokens[1] == "button":
                if self.tokens[2] == "count":
                    self.count = "_count"
                
                    if self.tokens[3] == "above":
                        self.type = "box"
        except:
            pass
        
    def render(self, context):
        print self.type
        print self.count
        
        badge = """
        <a name="fb_share" type="%s%s" href="http://www.facebook.com/sharer.php">Share</a>
        <script src="http://static.ak.fbcdn.net/connect.php/js/FB.Share" type="text/javascript"></script>
        """ % (self.type, self.count)
        
        
        return badge

def fbshare(parser, token):
    """

    """
    return FBShare(parser, token)

get_list = register.tag(fbshare)
