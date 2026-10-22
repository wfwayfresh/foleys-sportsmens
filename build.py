"""Foley's Sportsmens Inn website. Run `python3 build.py` to regenerate site/*.html.
The full menu lives in menu_data.py.
"""
from pathlib import Path
SITE = Path(__file__).parent / "site"
PHONE, TEL = "(248) 623-1122", "tel:+12486231122"
ADDR = "5864 Dixie Hwy, Clarkston, MI 48346"
MAPS = "https://www.google.com/maps/search/?api=1&query=Foley%27s+Sportsmens+Inn+5864+Dixie+Hwy+Clarkston+MI"
FB = "https://www.facebook.com/sportsmensgreatnorthern/"
NAV = [("index.html", "Home"), ("menu.html", "Food & Specials"), ("bar.html", "Bar & Happy Hour"), ("events.html", "Entertainment"), ("parties.html", "Private Events"), ("visit.html", "Visit")]
HOURS = [("Monday – Thursday", "11am – 9pm"), ("Friday – Saturday", "11am – 10pm"), ("Sunday", "12pm – 8pm")]

def page(fname, title, desc, body):
    nav = "".join(f'<a href="{h}"{" class=on" if h == fname else ""}>{t}</a>' for h, t in NAV)
    hrs = "<br>".join(f"{d}: {t}" for d, t in HOURS)
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@500;600;700&family=Playfair+Display:ital,wght@1,600&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css"><link rel="icon" href="images/logo.jpg">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"BarOrPub","name":"Foley's Sportsmens Inn","telephone":"+1-248-623-1122",
"address":{{"@type":"PostalAddress","streetAddress":"5864 Dixie Hwy","addressLocality":"Clarkston","addressRegion":"MI","postalCode":"48346"}},
"openingHours":["Mo-Th 11:00-21:00","Fr-Sa 11:00-22:00","Su 12:00-20:00"],"servesCuisine":["American","Bar food"],"sameAs":["{FB}"]}}</script></head><body>
<div class="topbar"><span>Food & Spirits · Clarkston, Michigan</span><span>Open daily · <a href="{TEL}">{PHONE}</a></span></div>
<header class="hdr"><a class="brand" href="index.html"><img src="images/logo.jpg" alt="Foley's Sportsmens Inn Food & Spirits logo"></a>
<button class="burger" aria-label="Menu" aria-expanded="false" onclick="this.parentElement.classList.toggle('open')"><span></span><span></span><span></span></button>
<nav>{nav}<a class="btn" href="parties.html#inquire">Book an Event</a></nav></header>
<div class="soon"><b>Online ordering coming soon!</b> For now, call <a href="{TEL}">{PHONE}</a> to place your order.</div>
<main>{body}</main>
<footer class="ftr"><div class="fwrap">
<div><img class="flogo" src="images/logo.jpg" alt="Foley's Sportsmens Inn"><p>Food, a full bar and every game on, on Dixie Highway in Clarkston.</p></div>
<div><h4>Find us</h4><p><a href="{MAPS}">{ADDR}</a><br><a href="{TEL}">{PHONE}</a></p></div>
<div><h4>Hours</h4><p>{hrs}</p></div>
<div><h4>Follow</h4><p><a href="{FB}">Facebook</a></p></div></div></footer></body></html>"""

HOME = f"""
<section class="hero" style="background-image:url(images/bar.jpg)"><div class="hero-in">
<p class="kicker">Clarkston's neighborhood inn</p>
<h1>Good food.<br>Cold drinks.<br><em>Every game on.</em></h1>
<p class="lede">A full bar, a newly remodeled dining room, all-season rooms full of TVs, and a kitchen turning out weekend specials worth the drive.</p>
<div class="ctas"><a class="btn big" href="menu.html">This week's specials</a><a class="btn line big" href="{TEL}">Call {PHONE}</a></div></div></section>

<section class="ticker"><div><b>Every day</b><span>Happy hour 11am–6pm</span></div><div><b>Friday</b><span>All-you-can-eat fish & chips</span></div><div><b>Every 1st and 3rd Saturday</b><span>Karaoke with DJ Rybo</span></div><div><b>Lions games</b><span>BOGO boneless wings</span></div></section>

<section class="wrap split"><div>
<p class="kicker">Newly remodeled</p><h2>Bright, open, and still the Foley's you know.</h2>
<p>The remodel brought in walls of windows and natural light, a bigger bar, and all-season rooms where you can catch the game in any weather. Come for a casual lunch, a night at the bar, or a celebration with the whole family.</p>
<blockquote>"Foley's got an absolutely gorgeous remodel. The restaurant is bright and feels alive. The windows let in so much natural light."<cite>Google review</cite></blockquote>
</div><figure><img src="images/banquet.jpg" alt="The bright dining room set for an event" loading="lazy"></figure></section>

<section class="dark"><div class="wrap"><p class="kicker">From the kitchen</p><h2>Specials that keep regulars coming back</h2>
<div class="cards">
<div class="card"><img src="images/fish-chips.jpg" alt="Fish and chips" loading="lazy"><h3>All-You-Can-Eat Fish & Chips</h3><p>Every Friday.</p></div>
<div class="card"><img src="images/scallops.jpg" alt="Pan seared scallops with asparagus" loading="lazy"><h3>Pan-Seared Scallops</h3><p>Silky potato purée, asparagus, Brussels sprouts, red wine reduction.</p></div>
<div class="card"><img src="images/sw-bowl.jpg" alt="Southwest chicken bowl" loading="lazy"><h3>Southwest Chicken Bowl</h3><p>Grilled chicken, rice, avocado and house-made cilantro crema.</p></div>
<div class="card"><img src="images/cheesecake.jpg" alt="Tiramisu cheesecake" loading="lazy"><h3>Tiramisu Cheesecake</h3><p>House-made espresso sauce and coffee-soaked ladyfingers.</p></div>
</div><p class="center"><a class="btn" href="menu.html">See more specials</a></p></div></section>

<section class="wrap split rev"><figure class="flyer"><img src="images/plant-bingo.jpg" alt="Plant Bingo night flyer" loading="lazy"></figure><div>
<p class="kicker">Always something going on</p><h2>Plant Bingo, karaoke & live music</h2>
<p>Plant Bingo nights sell out fast, with everyone going home with a plant. Karaoke with DJ Rybo takes over the first Saturday of the month, and live music drops in throughout the year.</p>
<a class="btn" href="events.html">What's coming up</a></div></section>

<section class="band"><div class="wrap split"><div>
<p class="kicker gold">Celebrations</p><h2>Two private spaces for your party</h2>
<p>Rehearsal dinners, showers, birthdays and holiday parties. Call and ask for Jen, and she'll help make it perfect.</p>
<a class="btn gold" href="parties.html#inquire">Send an event inquiry</a></div>
<figure><img src="images/table-set.jpg" alt="A long table set for a private party" loading="lazy"></figure></div></section>
"""

from html import escape as _e
import menu_data as _m
def _price(p):
    return "" if not p else '<span class="mp">' + _e(p if any(c.isalpha() for c in p) else "$" + p) + "</span>"
_jump = "".join(f'<a href="#{sid}">{_e(t)}</a>' for sid, t, *_ in _m.SECTIONS)
_SECIMG = {"appetizers":("wings-bonein.jpg","Bone-in chicken wings with celery"),"burgers":("burger.jpg","A Certified Angus Beef burger with onion straws and fries"),"pizza":("pizza.jpg","A Foley's pizza"),"entrees":("fish-chips.jpg","Beer-battered fish and chips with lemon"),"pasta":("pasta.jpg","A linguine pasta entrée with garlic bread"),"salads":("salad.jpg","A grilled chicken salad")}
_FEAT = [
 ("pizza.jpg","Pizza","16\" deep dish or 18\" round, nine house pizzas or build your own.","$22","#pizza"),
 ("burger.jpg","Certified Angus Beef burgers","Half-pound burgers on pretzel or brioche, with endless fries.","$15–16","#burgers"),
 ("fish-chips.jpg","Friday fish & chips","Wild-caught Atlantic fish in beer batter. All-you-can-eat every Friday.","$19","#entrees"),
 ("pasta.jpg","Pasta entrées","Served with garlic bread and a house salad or blue cheese coleslaw.","$16–21","#pasta"),
 ("wings-boneless-2.jpg","Chicken wings","Boneless or bone-in, same great price. Plain or tossed in Hot, BBQ, Sweet Asian Chili, Garlic Parmesan or Chipotle BBQ.","$12","#appetizers"),
 ("cocktail.jpg","Happy hour, every day","$2.50 domestics 11–2, $3 domestics 2–6.","Daily","bar.html"),
]
_feat = '<section class="feat"><div class="wrap"><p class="kicker">House favorites</p><h2>Start here</h2><div class="fgrid">' + "".join(
  f'<a class="fcard" href="{h}"><img src="images/{i}" alt="{_e(t)}" loading="lazy"><div><div class="mh"><h3>{_e(t)}</h3><span class="mp">{_e(pr)}</span></div><p>{_e(d)}</p></div></a>'
  for i, t, d, pr, h in _FEAT) + '</div></div></section>'
_secs = ""
for sid, title, note, items in _m.SECTIONS:
    its = "".join(f'<div class="mi"><div class="mh"><h3>{_e(n)}</h3>{_price(pr)}</div><p>{_e(d)}</p></div>' for n, d, pr in items)
    _img = (f'<img class="mban" src="images/{_SECIMG[sid][0]}" alt="{_e(_SECIMG[sid][1])}" loading="lazy">' if sid in _SECIMG else "")
    _secs += f'<section class="msec" id="{sid}">{_img}<h2>{_e(title)}</h2>{f"<p class=mnote>{_e(note)}</p>" if note else ""}<div class="mgrid">{its}</div></section>'
MENU = f"""
<section class="pagehead" style="background-image:url(images/scallops-2.jpg)"><div><p class="kicker">Food & specials</p><h1>The Foley's menu</h1><p>Gluten-free pizza, buns, bread and pasta available. Ask about today's chef's specials.</p></div></section>
<nav class="mjump">{_jump}<a href="#specials">Specials</a></nav>
<section class="soonbox"><div><p class="kicker">Coming soon</p><h2>Online ordering is on the way</h2><p>We're setting up online ordering so you can order ahead right from this page. Until then, give us a call and we'll have it ready.</p><a class="btn big" href="{TEL}">Call {PHONE} to order</a></div></section>
{_feat}
<section class="wrap">
{_secs}
<section class="msec" id="specials"><h2>Weekly & recurring</h2><div class="mgrid">
<div class="mi"><div class="mh"><h3>All-You-Can-Eat Fish & Chips</h3><span class="mp">Fridays · $19</span></div><p>A Friday tradition.</p></div>
<div class="mi"><div class="mh"><h3>Prime Rib</h3><span class="mp">Saturdays 4pm-close</span></div><p>A full pound with au jus, baked potato, broccoli and a side salad.</p></div>
<div class="mi"><div class="mh"><h3>BOGO Boneless Wings</h3><span class="mp">Lions games</span></div><p>Buy one, get one free during any Lions game.</p></div>
</div><h2>Recent chef's specials</h2><div class="mgrid">
<div class="mi"><div class="mh"><h3>Pan-Seared Scallops</h3></div><p>Potato purée, asparagus, Brussels sprouts, finished with a red wine reduction.</p></div>
<div class="mi"><div class="mh"><h3>Southwest Chicken Bowl</h3></div><p>Grilled chicken, rice, red onions, tomato, avocado and house-made cilantro crema.</p></div>
<div class="mi"><div class="mh"><h3>Hand-Battered Frog Legs</h3></div><p>Paired with a zesty Creole sauce.</p></div>
<div class="mi"><div class="mh"><h3>Tiramisu Cheesecake</h3></div><p>House-made espresso sauce and coffee-soaked ladyfingers between rich cheesecake.</p></div>
</div></section>
<p class="fine">Menu and prices as of {_m.UPDATED}; subject to change. Consuming raw or undercooked meats, poultry, seafood, shellfish, or eggs may increase the risk of foodborne illness.</p>
</section>"""

BAR = """
<section class="pagehead" style="background-image:url(images/bar.jpg)"><div><p class="kicker">The bar</p><h1>Happy hour, every single day</h1></div></section>
<section class="wrap split"><div>
<div class="hh"><h3>11am – 2pm</h3><ul><li>Domestics <b>$2.50</b></li><li>Premiums <b>$3</b></li><li>Well liquor <b>$3</b></li></ul>
<h3>2pm – 6pm</h3><ul><li>Domestics <b>$3</b></li><li>Premiums <b>$3.50</b></li><li>Well liquor <b>$3.50</b></li></ul></div>
<p class="small">Domestics include Budweiser, Bud Light, Miller Lite, Coors Lite, Miller High Life, PBR, Rolling Rock and Busch Light. Premiums include Michelob Ultra, Labatt and Molson.</p>
<p>A fully stocked bar, TVs on every wall, and all-season rooms for game day, any day of the year.</p>
</div><figure class="flyer"><img src="images/happy-hour.jpg" alt="Foley's every day happy hour board" loading="lazy"></figure></section>
<section class="wrap"><div class="gallery"><img src="images/cocktail.jpg" alt="A cocktail" loading="lazy"><img src="images/booths.jpg" alt="Booths and TVs" loading="lazy"><img src="images/st-pats.jpg" alt="Staff celebrating St. Patrick's Day" loading="lazy"></div></section>"""

EVENTS = """
<section class="pagehead" style="background-image:url(images/st-pats.jpg);background-position:center 28%"><div><p class="kicker">Entertainment schedule</p><h1>Come for dinner, stay for the fun</h1></div></section>
<section class="wrap split"><div>
<h2>Plant Bingo</h2><p>Hosted with My Artful Studio: ten rounds of bingo where plants are the prizes, plus raffles and giveaways. Everyone gets a plant when they arrive. Bingo nights come with specials like half-price appetizers and desserts and $4 cocktails.</p>
<p><b>These sell out.</b> Watch our Facebook for the next date and grab your seat early.</p>
</div><figure class="flyer"><img src="images/plant-bingo.jpg" alt="Plant Bingo flyer" loading="lazy"></figure></section>
<section class="dark"><div class="wrap split rev"><figure class="flyer"><img src="images/karaoke.jpg" alt="Karaoke with DJ Rybo flyer" loading="lazy"></figure><div>
<h2>Karaoke with DJ Rybo</h2><p class="big">First Saturday of the month · 8:30pm – midnight</p><p>Grab the mic or just cheer everyone else on.</p>
<h2>Live music & game days</h2><p>Live acoustic nights pop up throughout the year, and every Lions game comes with buy-one-get-one boneless wings.</p></div></div></section>"""

PARTIES = f"""
<section class="pagehead" style="background-image:url(images/banquet.jpg)"><div><p class="kicker">Private events</p><h1>Celebrate at Foley's</h1></div></section>
<section class="wrap split"><div>
<h2>Two separate spaces</h2>
<p>We have two private spaces for holiday parties, rehearsal dinners, showers, birthdays and every kind of special occasion. Large groups are always welcome.</p>
<p><b>Call {PHONE} and ask for Jen</b> to book. She'll help with every detail.</p>
<blockquote>"Held our wedding rehearsal dinner at Foley's and it was fantastic. Jen was so helpful and helped make our event perfect… Food was great, staff was excellent."<cite>Facebook review</cite></blockquote>
<a class="btn" href="#inquire">Send an inquiry</a></div>
<figure><img src="images/table-set.jpg" alt="Long table set for a party" loading="lazy"></figure></section>
<section class="dark" id="inquire"><div class="wrap split"><div>
<p class="kicker">Event inquiry</p><h2>Tell us about your event</h2>
<p>Fill this out and we'll get back to you to check availability and plan the details. Prefer to talk? Call {PHONE} and ask for Jen.</p>
</div>
<form class="inq" id="inqform" novalidate>
<input type="hidden" name="_subject" value="New event inquiry: Foley's Sportsmens Inn website">
<input type="hidden" name="_template" value="table">
<input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off">
<label>Your name<input name="Name" required autocomplete="name"></label>
<div class="row"><label>Phone<input name="Phone" type="tel" required autocomplete="tel"></label>
<label>Email<input name="Email" type="email" required autocomplete="email"></label></div>
<div class="row"><label>Date of event<input name="Event date" type="date" required></label>
<label>Number of guests<input name="Number of guests" type="number" min="1" required></label></div>
<label>What are you celebrating?<select name="Celebration" required><option value="">Choose one</option><option>Birthday</option><option>Rehearsal dinner</option><option>Wedding or engagement</option><option>Baby or bridal shower</option><option>Graduation</option><option>Holiday party</option><option>Work or team event</option><option>Memorial or celebration of life</option><option>Other</option></select></label>
<label>Notes or comments<textarea name="Notes" rows="4" placeholder="Time of day, food or drink ideas, anything we should know"></textarea></label>
<button class="btn big" type="submit">Send inquiry</button>
<p class="formmsg" id="inqmsg" role="status"></p>
</form></div></section>
<script>
document.getElementById('inqform').addEventListener('submit',async e=>{{
 e.preventDefault();const f=e.target,m=document.getElementById('inqmsg');
 if(!f.checkValidity()){{f.reportValidity();return}}
 m.textContent='Sending…';
 try{{const r=await fetch('https://formsubmit.co/ajax/kurko@att.net',{{method:'POST',headers:{{'Accept':'application/json'}},body:new FormData(f)}});
  const j=await r.json(); if(String(j.success)==='true'){{f.reset();m.textContent="Thank you! We got your inquiry and will be in touch soon."}} else {{m.textContent="Sorry, that didn't go through. Please call {PHONE}."}}
 }}catch(err){{m.textContent="Sorry, that didn't go through. Please call {PHONE}."}}
}});
</script>
<section class="wrap"><div class="gallery"><img src="images/dining.jpg" alt="Floral centerpiece" loading="lazy"><img src="images/centerpiece.jpg" alt="Table detail" loading="lazy"><img src="images/banquet.jpg" alt="Dining room set for an event" loading="lazy"></div></section>"""

VISIT = f"""
<section class="pagehead" style="background-image:url(images/exterior-2.jpg)"><div><p class="kicker">Visit</p><h1>On Dixie Highway in Clarkston</h1></div></section>
<section class="wrap split"><div>
<h2>Hours</h2><table class="hours">{"".join(f"<tr><td>{d}</td><td>{t}</td></tr>" for d, t in HOURS)}</table>
<h2>Address</h2><p><a href="{MAPS}">{ADDR}</a></p>
<h2>Reservations</h2><p><a class="btn" href="{TEL}">{PHONE}</a></p><p class="small">Walk-ins always welcome.</p>
</div><iframe class="map" title="Map to Foley's" loading="lazy" src="https://www.google.com/maps?q=Foley%27s+Sportsmens+Inn,+5864+Dixie+Hwy,+Clarkston,+MI&output=embed"></iframe></section>"""

for f, t, d, b in [
    ("index.html", "Foley's Sportsmens Inn · Food & Spirits in Clarkston, MI", "Full bar, daily happy hour, weekly specials, Friday all-you-can-eat fish & chips, private party rooms. 5864 Dixie Hwy, Clarkston.", HOME),
    ("menu.html", "Food & Specials · Foley's Sportsmens Inn", "Friday all-you-can-eat fish & chips, prime rib, scallops and chef's specials at Foley's in Clarkston.", MENU),
    ("bar.html", "Bar & Happy Hour · Foley's Sportsmens Inn", "Happy hour every day: $2.50 domestics 11–2, $3 domestics 2–6 at Foley's Clarkston.", BAR),
    ("events.html", "Entertainment Schedule: Plant Bingo, Karaoke & More · Foley's Sportsmens Inn", "Plant Bingo, karaoke with DJ Rybo, live music and Lions game specials at Foley's.", EVENTS),
    ("parties.html", "Private Events · Foley's Sportsmens Inn", "Two private spaces for parties, showers and rehearsal dinners. Call and ask for Jen.", PARTIES),
    ("visit.html", "Hours & Directions · Foley's Sportsmens Inn", "Foley's Sportsmens Inn, 5864 Dixie Hwy, Clarkston MI. Hours and reservations.", VISIT)]:
    (SITE / f).write_text(page(f, t, d, b))
print("built")
