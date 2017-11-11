<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
		<title>{{info.title()}}</title>
    </head>
    <body>
    % if info.message() != "":
        <div style="background-color: rgba(255,0,0,0.4)">
            <p style="margin: none">{{info.message()}}</p>
        </div>
    % end
    % if info.site() == "home":
        <p style="display: none;">
            {{info.prev_site("home")}}
        </p>
        <div style="texte-align: center;">
            <h1>Velkominn í Heimasíðuna</h1>
            <div>
                 <form style="display: flex; Justify=content: space-around;" method="post" action="/">
                    <p style="display: none;">
                        {{info.site("sign_up")}}
                        {{info.title("Sign Up")}}
                    </p>
                    <input style="display: none;" type="text" name="info" value="{{str(info.info())}}">
                    <input type="submit" value="Sign Up">
                </form>
                 <form style="display: flex; Justify=content: space-around;" method="post" action="/">
                     <p style="display: none;">
                        {{info.site("login")}}
                        {{info.title("Login")}}
                    </p>
                    <input style="display: none;" type="text" name="info" value="{{str(info.info())}}">
                    <input type="submit" value="  Login  ">
                </form>
            </div>
        </div>
    % elif info.site() == "sign_up":
        <form style="texte-align: center;" method="post" action="/">
            <h1>Sign Up</h1>
            <p style="display: none;">
                {{info.prev_site("sign_up")}}
                {{info.site("home")}}
                {{info.title("Home")}}
            </p>
            <input style="display: none;" type="text" name="info" value="{{str(info.info())}}">
            <input type="text" name="user" placeholder="Notandanafn" pattern="^[^#*<>&quot;'\{\}\[\];]+$" title="Text may not contain any malicious characters" maxlength=32 required><br>
            <input type="password" name="pass" placeholder="Password" pattern="^[^#*<>&quot;'\{\}\[\];]+$" title="Text may not contain any malicious characters"  maxlength=32 required><br>
            <input type="submit">
        </form>
    % elif info.site() == "login":
        <form style="texte-align: center;" method="post" action="/">
            <h1>Login</h1>
            <p style="display: none;">
                {{info.prev_site("login")}}
                {{info.site("home")}}
                {{info.title("Home")}}
            </p>
            <input style="display: none;" type="text" name="info" value="{{str(info.info())}}">
            <input type="text" name="user" placeholder="Notandanafn" pattern="^[^#*<>&quot;'\{\}\[\];]+$" title="Text may not contain any malicious characters" maxlength=32 required><br>
            <input type="password" name="pass" placeholder="Password" pattern="^[^#*<>&quot;'\{\}\[\];]+$" title="Text may not contain any malicious characters"  maxlength=32 required><br>
            <input type="submit">
        </form>
    % else:
        <h1>Þessi síða ætti aldrei að byrtast</h1>
    % end
    </body>
</html>
