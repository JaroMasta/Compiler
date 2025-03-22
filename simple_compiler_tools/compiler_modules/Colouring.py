class Colouring:
    html_start = '''
    <!DOCTYPE html>
    <html lang="pl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Podświetlanie składni</title>
        <style>
            body { font-family: Consolas, monospace; background-color: #f5f5f5; padding: 20px; }
            pre { background: #2d2d2d; padding: 10px; border-radius: 5px; color: #ffffff; }
            .NUMBER { color: #B5CEA8; }
            .KEYWORD { color: #9CDCFE; }
            .Operator { color: #C586C0; }
            .ERROR { color: #f13710;}
            .LPAREN { color: #C586C0; }
            .RPAREN { color: #C586C0; }
        </style>
    </head>
    <body>
        <pre>'''
    
    html_end = '''</body> </html>'''

    # generates html snippet for one token
    def color_token(self, token : str, value : str) -> str:
        return "<span class=\""+ token +"\">" + value + "</span>"
    
    # generowanie pokolorowanego kodu
    def generate_html(self, arr : list) -> None:
        html_full : str = self.html_start
        for token_value in arr:
            html_full += self.color_token(token_value[0], token_value[1])
        html_full += self.html_end
        with open("kolorowanie.html", "w", encoding="utf-8") as file:
            file.write(html_full)