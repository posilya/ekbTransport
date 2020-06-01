#-*- coding: utf-8 -*-
import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = "text/html; charset=UTF-8"
        self.response.write('''
            <!DOCTYPE hmtl>
            <html prefix="og: http://ogp.me/ns#" lang="ru">
            	<head>
            		<meta charset="utf-8">
            		<meta name="viewport" content="width=device-width, initial-scale=1">
            		<title>Транспрот Екатеринбурга</title>
            		<meta property="og:title" content="Транспрот Екатеринбурга">
            		<meta property="og:description" content="Неофициально">
            		<meta property="og:site_name" content="Транспрот Екатеринбурга">
            		<meta property="og:type" content="website">
            		<meta property="og:url" content="ekbtransport.appspot.com">
            		<!-- Картин очки -->
            		<meta property="og:image" content="ekbtransport.appspot.com/og/image.png">
            		<meta property="vk:image" content="ekbtransport.appspot.com/og/vk.png">
            		<meta property="fb:image" content="ekbtransport.appspot.com/og/fb.png">
            		<meta property="twitter:image" content="ekbtransport.appspot.com/og/twitter.png">
            		<meta property="og:image:width" content="1200">
            		<meta property="og:image:height" content="630">
            		<!-- Шрифтеки -->
            		<link href="https://fonts.googleapis.com/css2?family=Fira+Sans:ital,wght@0,400;0,700;1,400;1,700&display=swap" rel="stylesheet">
            		<!-- Стайлы -->
            		<style rel="stylesheet" type="text/css">
            			@media screen and (min-width: 480px) {
            				/* Компьютерики */
            				body {
            					max-width: 500px;
            					padding: 20px;
            				}

            				.links img {
            					margin-top: -40px;
            					height: 100%;
            					cursor: pointer;
            					float: right;
            					opacity: 0;
            					transition: .2s opacity;
            				}

            				.twtr:hover img,
            				.tlgrm:hover img,
            				.inst:hover img,
            				.fb:hover img,
            				.vk:hover img {
            					opacity: 1;
            				}

            				#qr {
            					width: calc(100vw - 120px);
            					height: calc(100vh - 120px);
            					position: absolute;
            					top: 60px;
            					left: 60px;
            					background-color: black;
            					border-radius: 20px;
            					box-shadow: 0 0 120px 60px #393939;
            				}

            				#qr button {
            					padding: 0;
            					width: 30px;
            					height: 30px;
            					margin: 15px;
            					float: right;
            					border: 2px solid #d9d9d9;
            					border-radius: 15px;
            					background-color: black;
            					background-image: url('https://ekbtransport.appspot.com/close.svg');
            					background-repeat: no-repeat;
            					background-position: center;
            					transition: .3s background-color, .3s border-color;
            				}

            				#qr button:hover {
            					background-color: red;
            					border-color: white;
            				}

            				#qr button:active {
            					background-color: #b00;
            					border-color: white;
            				}

            				#qr div {
            					width: 50%;
            					position: absolute;
            					left: 50%;
            					top: 50%;
            					-webkit-transform: translate(-50%, -50%);
            					-moz-transform: translate(-50%, -50%);
            					-ms-transform: translate(-50%, -50%);
            					-o-transform: translate(-50%, -50%);
            					transform: translate(-50%, -50%);
            				}

            				#qrCode {
            					width: 50%;
            					display: block;
            					margin: 0 auto;
            				}

            				#socialName {
            					font-weight: bold;
            					text-align: center;
            					font-size: 2em;
            					margin-bottom: 5px
            				}

            				#atNick {
            					text-align: center;
            					font-size: 1.25em;
            					margin-top: 5px;
            				}

            				#message {
            					display: table;
            					margin: 0 auto;
            					padding: 10px;
            					background-color: yellow;
            					color: black;
            					border-radius: 10px 10px 10px 0;
            					box-shadow: 0 0 30px 1px #990;
            				}
            			}

            			@media screen and (max-width :479px) and (orientation: portrait) {
            				/* Телефончики */
            				body {
            					width: 90%;
            					padding: 15px 0;
            				}

            				.links img {
            					display: none;
            				}
            			}

            			html {
            				min-height: 100%;
            			}

            			body {
            				height: inherit;
            				background-color: black;
            				color: #d9d9d9;
            				font-family: "Fira Sans", sans-serif;
            				margin: 0 auto;
            			}

            			.logo {
            				max-width: 230px;
            			}

            			.links {
            				width: 50%
            			}

            			.links div {
            				height: 40px;
            				line-height: 40px;
            				margin: 10px 0;
            				background-size: 100% 78px;
            				background-position: center top;
            				background-repeat: no-repeat;
            				transition: .3s background-position, .3s color;
            			}

            			.links a {
            				color: #d9d9d9;
            				text-decoration: none;
            			}

            			.twtr {
            				background-image: linear-gradient(180deg, black 38px, #1DA1F2 38px);
            			}

            			.tlgrm {
            				background-image: linear-gradient(180deg, black 38px, #0088cc 38px);
            			}

            			.inst {
            				background-image: linear-gradient(180deg, black 38px, #C13584 38px, #e1306c 58px, #fd1d1d 78px);
            			}

            			.fb {
            				background-image: linear-gradient(180deg, black 38px, #4267B2 38px);
            			}

            			.vk {
            				background-image: linear-gradient(180deg, black 38px, #4680C2 38px);
            			}

            			.twtr:hover,
            			.tlgrm:hover,
            			.inst:hover,
            			.fb:hover,
            			.vk:hover  {
            				background-position: center bottom;
            			}

            			.links a {
            				padding-left: 10px;
            				display: block;
            				width: calc(100% - 50px);
            				height: 100%;
            			}

            			.twtr:hover a,
            			.tlgrm:hover a,
            			.inst:hover a,
            			.fb:hover a,
            			.vk:hover a {
            				color: white;
            			}
            		</style>
            	</head>
            	<body>
            		<img class="logo" src="https://ekbtransport.appspot.com/logo.svg">
            		<p class="description">Неофициально</p>
            		<p style="display: none;">Пока тут только ссылки на соцсети, но дальше будет также, потому что оптимизм.</p>
            		<div class="links">
            			<div class="twtr"><a href="https://twitter.com/ekbtrans">Твиттер</a><img src="https://ekbtransport.appspot.com/qr.svg" onclick="qr(0)"></div>
            			<div class="tlgrm"><a href="tg://resolve?domain=ekbTrans">Telegram</a><img src="https://ekbtransport.appspot.com/qr.svg" onclick="qr(1)"></div>
            			<div class="inst"><a href="https://instagram.com/ekbtrans">Instagram</a><img src="https://ekbtransport.appspot.com/qr.svg" onclick="qr(2)"></div>
            			<div class="fb"><a href="http://facebook.com/ekbtrans">Facebook</a><img src="https://ekbtransport.appspot.com/qr.svg" onclick="qr(3)"></div>
            			<div class="vk"><a href="https://vk.com/ekbTransport">ВКонтакте</a><img src="https://ekbtransport.appspot.com/qr.svg" onclick="qr(4)"></div>
            		</div>
            		<div id="qr" style="display: none;">
            			<button onclick="win.style.display = 'none';"></button>
            			<div>
            				<img id="qrCode" alt="qr-код" src="qr.svg" style="border: 2px solid #d9d9d9; border-radius: 20px;">
            				<p id="socialName">Название соцсети</p>
            				<p id="atNick">@ник в соцсети</p>
            				<p id="message">Если ты это видишь, напиши мне</p>
            			</div>
            		</div>
            	</body>
            	<script type="text/javascript">
            		var win  = document.getElementById('qr');
            		var qrC  = document.getElementById('qrCode');
            		var sn   = document.getElementById('socialName');
            		var nick = document.getElementById('atNick');

            		function qr(qrN) {
            			document.getElementById('message').style.display = 'none';
            			qrC.style = '';
            			switch (qrN) {
            				case 0:
            					qrC.src = "https://ekbtransport.appspot.com/qr/Twitter.svg";
            					sn.innerHTML = "Twitter";
            					nick.innerHTML = "@ekbTrans";
            					break;
            				case 1:
            					qrC.src = "https://ekbtransport.appspot.com/qr/Telegram.svg";
            					sn.innerHTML = "Telegram";
            					nick.innerHTML = "@ekbTrans";
            					break;
            				case 2:
            					qrC.src = "https://ekbtransport.appspot.com/qr/Instagram.svg";
            					sn.innerHTML = "Instagram";
            					nick.innerHTML = "@ekbtrans";
            					break;
            				case 3:
            					qrC.src = "https://ekbtransport.appspot.com/qr/Facebook.svg";
            					sn.innerHTML = "Facebook";
            					nick.innerHTML = "@ekbTrans";
            					break;
            				case 4:
            					qrC.src = "https://ekbtransport.appspot.com/qr/VK.svg";
            					sn.innerHTML = "VK";
            					nick.innerHTML = "@ekbtransport";
            					break;
            			}
            			win.style.display = 'block';
            		}
            	</script>
            </html>
        ''')

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
