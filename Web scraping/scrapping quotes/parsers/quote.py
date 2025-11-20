from locators.quote_locators import quotes_locators

class quote_parser:
      """
      Given one of the specific quote divs, find out the data about the quote (quote content, author, tags)

      """
      def __init__(self,parent):
            self.parent = parent
        
      def __repr__(self):
            return f'<Quote {self.content}, by {self.author}>'

      @property
      def content(self):
            locator = quotes_locators.content
            return self.parent.select_one(locator).string
      
      @property
      def author(self):
            locator = quotes_locators.author
            return self.parent.select_one(locator).string
      
      @property
      def tags(self):
            locator = quotes_locators.tags
            return [e.strings for e in self.parent.select_one(locator)]
        