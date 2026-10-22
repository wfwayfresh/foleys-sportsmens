"""Foley's full menu — every item and price from the printed menu.
To update the menu, edit this file (everything else renders
from it). Each item: (name, description, price_text)."""

UPDATED = "October 2026"

SECTIONS = [
 ("appetizers", "Appetizers", "", [
  ("Fried Pickles", "Dill pickle spears lightly battered, deep-fried golden brown and served with in-house made bistro sauce.", "11"),
  ("Chicken Wings", "Boneless or bone in, same great price, served plain or tossed in any of our sauces: Hot, BBQ, Sweet Asian Chili, Garlic Parmesan, Chipotle BBQ.", "12"),
  ("Fried-Cheese Ravioli", "These are served with Italian herb-tomato dipping sauce.", "10"),
  ("Bavarian Pretzel Bites & Beer Cheese", "Warm Bavarian soft pretzel bites, salted and served with our savory and creamy craft beer cheese sauce.", "11"),
  ("Buffalo Chicken Dip", "Shredded chicken, tangy buffalo sauce and a creamy cheese blend served with an array of in-house made tortilla chips.", "12"),
  ("Bones in a Basket", "A basket full of char-grilled, slow-roasted BBQ rib bones. (Yes, we leave the meat on them!) These are finger-lickin' good!", "12"),
  ("Quesadilla", "Flour tortilla stuffed with cheddar jack cheese served with a side of salsa and sour cream. Add chicken or add pork +5.", "9"),
  ("Garlic Breadsticks", "Fresh out of the oven, hot and steamy, served with cheese dip.", "9"),
  ("Butterflied Battered Shrimp", "Lightly battered basket full of butterflied shrimp served with a side of zesty cocktail sauce.", "11"),
  ("Chicken Tenders", "Would our menu be complete if we did not offer our all-time favorite: boneless chicken tenders served with your choice of dipping sauce!", "12"),
  ("Mozzarella Sticks", "Sliced mozzarella cheese rolled in a delicate breadcrumb batter, served with marinara.", "10"),
  ("Chile Con Queso", "Our own special blend of melted cheeses and peppers served with an array of in-house made tortilla chips.", "11"),
 ]),
 ("salads", "Salads", "Dressing choices: Ranch, Thousand Island, Honey Mustard, Italian, Bleu Cheese, Balsamic Vinaigrette, Raspberry Vinaigrette, Greek, Catalina, Caesar or Vinegar and Oil.", [
  ("The Wedge", "Our house salad is a wedge of iceberg lettuce served with diced tomato, crumbled blue cheese, bacon and topped with a balsamic glaze. Served with blue cheese dressing. With grilled chicken breast add 5.", "11"),
  ("Caesar Salad", "Just a good old Caesar salad with our little twist! Instead of traditional bread croutons we have substituted them with a fried cheese tortellini and then Parmesan cheese and a nice, rich Caesar dressing. You just have to give it a try! With grilled chicken add 5.", "12"),
  ("Greek Salad", "Traditional Greek salad served with beets, red onions, cucumbers, tomatoes, black olives, feta cheese and a traditional Greek dressing. With grilled chicken add 5.", "15"),
  ("Taco Salad", "Served in a crisp flour tortilla, lettuce, salsa, black olives, shredded cheddar jack cheese, seasoned ground beef, garnished with salsa and sour cream, served with Catalina dressing. With grilled chicken add 5.", "14"),
  ("Smoked Turkey Club Salad", "Wonderful smoked turkey breast with bacon, tomatoes and cheddar jack cheese served on a bed of spring mix with buttermilk ranch dressing.", "14"),
  ("Oriental Grilled Chicken", "We start with a mixture of lettuce and cabbage, then mix in crispy rice noodles, roasted red peppers, mandarin oranges and cucumbers then top that with grilled chicken with sesame oil dressing. Make it a salmon salad for 19.", "16"),
  ("Asiago Bread Bowl", "Mixed greens, chickpeas, black olives, tomato, ham, pepperoni and banana peppers served with a Greek olive oil dressing.", "16"),
  ("Magnificent Maurice Salad", "We combine ham, turkey, Swiss cheese and sweet gherkin pickles mixed with our house Maurice dressing served atop a bed of crisp iceberg and mixed greens.", "16"),
 ]),
 ("burgers", "Certified Angus Beef Burgers", "We make all of our half-pound Certified Angus Beef burgers and serve them with crisp lettuce, tomato, pickles and onions, on your choice of pretzel or brioche bun. All burgers are served with endless fries. Substitute sweet potato fries or house-made kettle chips for an additional 2. If you prefer, substitute a grilled ground turkey, veggie patty or chicken breast at no additional cost.", [
  ("Classic Cheeseburger", "This Certified Angus Beef burger with your choice of cheese: American, Swiss, pepper jack, cheddar or blue cheese crumbles.", "15"),
  ("Black & Blue", "Blue cheese and sautéed onions, with the Certified Angus Beef burger lightly coated with Cajun seasoning.", "15"),
  ("Swiss & Mushroom", "This old-time favorite Certified Angus Beef burger with sautéed mushrooms and onions then topped with melted Swiss cheese.", "15"),
  ("Southwestern", "This Certified Angus Beef burger is a bit of the South with fried jalapeños and pepper jack cheese and served with a side of salsa.", "15"),
  ("New Yorker", "Sure to sharpen your taste buds with this Certified Angus Beef burger, sharp New York cheddar and hickory-smoked bacon.", "15"),
  ("Signature Burger", "Half-pound Certified Angus Beef burger, strips of hickory-smoked bacon, sautéed mushrooms and onions topped with fresh lettuce, tomatoes, pickles and onion straws on our brioche bun, including Sriracha mayo on the side, and of course seasoned fries. Add cheese for 1.00.", "16"),
 ]),
 ("sandwiches", "Sandwiches & Such", "All sandwiches are served with French fries. Top any sandwich with our sweet potato fries or house-made potato chips for an additional 2.", [
  ("Philly Cheese Steak", "Old-fashioned Philly steak with grilled peppers, onions, mushrooms and melted Swiss cheese served on a hoagie bun.", "15"),
  ("Ham & Swiss", "Shaved ham stacked high with sautéed onions, served on flat bread, Swiss cheese melted over the top makes this a mouthwatering sandwich.", "14"),
  ("Grilled Chicken Caesar Sandwich", "Sliced, grilled chicken breast, tomatoes, romaine lettuce and parmesan cheese, all served on flat bread that has been drizzled with our own Caesar dressing.", "15"),
  ("Fish Sandwich", "Beer-battered fish fillet fried until golden brown, topped with blue cheese coleslaw and served on flat bread.", "15"),
  ("Smoked Turkey Club Croissant", "Thinly sliced smoked turkey breast with bacon, sliced onion, tomato, lettuce and a side of creamy dill sauce, all served on a croissant.", "14"),
  ("French Dip", "Thinly sliced beef sautéed with onions and topped with your favorite cheese and served with au jus sauce for dipping.", "15"),
  ("Pulled Pork", "Pulled pork in our own special bourbon-whiskey BBQ sauce and served on a brioche bun.", "15"),
  ("Traditional Beef Nacho", "This is a traditional beef nacho you soon will not forget! A plate full of fresh corn tortilla chips topped with fresh green peppers, onion and tomatoes. Then all of that is smothered in melted cheese.", "Ground beef 16 · Chicken or pork 17"),
 ]),
 ("pizza", "Pizza", "16\" deep dish or 18\" round: 22. Gluten free +4.", [
  ("Meat Lovers", "Every meat you could want on one pizza! Italian sausage, pepperoni, ham and ground beef topped with a mixture of mozzarella and cheddar jack cheeses.", ""),
  ("Greek", "Black olives, artichoke hearts, tomatoes and onions topped with a mix of feta and mozzarella cheeses.", ""),
  ("BBQ Chicken", "Has a tangy sauce with a hint of BBQ sauce with grilled chicken mixed in Sportsmens own BBQ sauce, with grilled onions and topped with mozzarella cheese.", ""),
  ("Vegetarian", "For you out there who love the fresh flavors of vegetables! There is artichoke hearts, onions, mushrooms, tomatoes and black olives topped with mozzarella cheese.", ""),
  ("Hawaiian", "Put on your grass skirt and wake up your taste buds for this one! Ham, pineapple and bacon topped with mozzarella cheese.", ""),
  ("Margherita", "Fresh mozzarella, tomatoes, virgin olive oil and fresh basil.", ""),
  ("B.L.T.", "Hot pizza with bacon and mozzarella and finished with cold ranch dressing, tomatoes and lettuce.", ""),
  ("Pesto Pizza", "Fresh pesto, tomatoes, red onions, black olives and parmesan cheese.", ""),
  ("Make Your Own", "This pizza is up to you! Choose FOUR toppings with cheese: bacon, ground beef, ham, Italian sausage, pepperoni, artichokes, black olives, crushed red peppers, feta cheese, tomatoes, hot pepper rings, green peppers, mushrooms, onions, pineapple or roasted red peppers. Add chicken 5. Additional items +3.", ""),
 ]),
 ("entrees", "Main Entrées", "All entrées served with your choice of a house salad or blue cheese coleslaw.", [
  ("Sizzling Fajita", "Sautéed onions and tri-colored peppers served on a sizzling platter with your choice of poultry or beef. A side of steamed flour tortillas, sour cream, salsa, refried beans and Spanish rice.", "Chicken 19 · Steak 21"),
  ("Chicken Potpie", "Good, old-fashioned, homemade chicken potpie with fresh garden vegetables and large chunks of chicken in creamy sauce topped with a light, airy pastry top.", "17"),
  ("Maple Syrup-Glazed Grilled Pork Chop", "A thick, juicy pork chop first marinated, then slowly grilled and glazed with a mixture of Jim Beam® and maple syrup, served with sautéed apples and toasted pecans with a side of oven roasted carrots.", "20"),
  ("Fish & Chips", "Wild-caught Atlantic fish lightly coated with beer batter and served with French fries and a side of blue cheese coleslaw or house salad. Friday special: all-you-can-eat 19.", "Two pieces 16 · Three pieces 17"),
  ("Grilled Salmon", "Charred, grilled salmon topped with our house-made cucumber-dill sauce and balsamic glaze served with wild rice and asparagus.", "21"),
  ("Jambalaya", "Andouille sausage, shrimp, chicken, tri-colored peppers, onions, tomatoes and rice along with our in-house special seasonings including a bit of Cajun, simmered to perfection. You will feel like you are in New Orleans.", "19"),
  ("Chicken Piccata", "Pan-seared, lightly dusted chicken breast with a traditional white wine, rich and buttery lemon-caper sauce served over linguine.", "19"),
 ]),
 ("pasta", "Pasta Entrées", "All pasta dishes are served with garlic bread and your choice of house salad or blue cheese coleslaw. Gluten-free pasta +3.", [
  ("Lemon Shrimp & Asparagus", "Start off with a lemon-cream sauce tossed with linguine pasta, garnished with sautéed shrimp and asparagus with a hint of dill.", "19"),
  ("Cheese Tortellini & Tomato Basil", "A wonderful cheese-filled tortellini that is tossed with a fresh, zesty tomato-basil sauce and topped with freshly grated Parmesan cheese.", "16 · Chicken 18 · Shrimp 19"),
  ("Chicken Alfredo", "Linguine noodles tossed in a flavorful sauce of roasted garlic, cream and parmesan cheese with a grilled chicken breast.", "18"),
  ("Rustic Tuscan Penne Pasta", "Delicately marinated grilled chicken breast or salmon served on a bed of penne pasta that has been tossed with olive oil-Tuscan seasonings and sautéed bell peppers, onions and black olives.", "Chicken 18 · Salmon 21"),
 ]),
]
