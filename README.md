<h2>My Yummy Dishes</h2>

The My Yummy Dishes website is database website, where an user can view their recipes and that of other users. An user must
register or Sign in before they are allowed to add, edit or delete recipes. When adding a recipe the user can, if they want to 
add an image of the recipe they are adding, but if they don't a default image will appear in its place.

Please <a href="">Click Here</a> to see the database schema.

<hr/> 

<h3>UX</h3>

<strong>Registration of user</strong> - The user can register themselves by the registration page where they are ask for an username and password.
                       If an username is already registered a message will appear to inform the user to choose a different 
                       username. When the user enters their password and misspell their password, a message will appear to inform 
                       them that their password does not match.

<strong>Sign in of user</strong> - The user can click on the Sign in button, which will take them to the sign in page and sign themselves in by
                  filling in the sign in form. If the user does not exists they will be redirected to the registration page to
                  register themselves. The user can sign in with their details and if the user misspell his username or password,
                  a message will appear to inform them that their details does not match.

<strong>Sign out of user</strong> - Once user has singed in and has used the website and they want to leave after cooking an amazing meal, adding,
                   editing or deleting of an recipe; the user can click on the Sign out button which will appear if they are signed in.
                   By clicking on the sign out button the user session will end.

<strong>Viewing of recipe</strong> - An user can click on the recipes name that is displayed on the home page, that will take them to that recipe only.
                    If the user wants to view any other recipe they need to click on the Category and all the recipes under that category
                    will appear on the category recipe page.

<strong>Add a recipe</strong> - Once the user has signed in and wants to add their favourite recipe their can do that by clicking on the Add recipe button,
               which takes them to the add recipe page. Here a user can fill in a form which consists of the category, recipes name,
               image of recipe, Ingredients, Method, prep-time, cooking time and serving how many people.

<strong>Edit a recipe</strong> - Once the user has signed in and wants to edit their favourite recipe their can do that by clicking on the edit button which 
                takes them to the edit recipe page. Here a user can fill in a form which consists of the category, recipes name , image of recipe,
                Ingredients, Method, prep-time, cooking time and serving how many people.

<strong>Delete recipe</strong> - If an user decides to delete a reicpe, they can do so by clicking on the delete button and that recipe will be deleted from
                the database. Then a message will appear stating the recipe has been deleted. 

<hr/> 

<h3>Design</h3>

I have used the a program called Figma that helped design the pages and this makes them easy to use and keeps them uncluttered.
The user can see and read everything clearly without having to do an indepth search for what the are looking for. The approach to the design was to make
the website easy to navigate and inviting so anyone can use this with ease.

I have changed the placemnent of the header image to the body image and the shape of the cards.

Please <a href="">Click Here</a> to see the design.

<hr/> 

<h3>Features</h3>

<ul>
    <li>Dropdown menu for all the categories.</li>
    <li>Registration and Sign in links for the user to register or sign in.</li>
    <li>On the home page an Add recipe link for the user to add more recipes to the database.</li>
    <li>The ability for the user to edit and delete recipes on the database.</li>
    <li>Each recipe can be displayed on their own page, to list everything about the recipe.</li>
</ul>    

<hr/> 

<h3>Technology</h3>

<h4>Langauges</h4>
    <ul>
        <li><a href="https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5">HTML5</a>: was used for the rendering of the template design.</li>
        <li><a href="https://www.w3schools.com/css/">CSS3</a>: was used for the rendering of the template style.</li>
        <li><a href="https://www.python.org/">Python</a>: was used for the rendering of the application logic.</li>
    </ul>
<h4>Database</h4>
    <ul>
        <a href="https://www.mongodb.com/">MongoDB</a>: was used for the database.
    </ul>   
<h4>Frameworks</h4>
    <ul>
        <li><a href="https://flask.palletsprojects.com/en/1.1.x/">Flask</a>: was used for creating routes and the rendering of the HTML5 templates.</li>
        <li><a href="https://getbootstrap.com/">Bootstrap</a>: was used for the navigation, login templates and responsiveness.</li>
    </ul>
<h4>Tools</h4>
    <ul>
        <li><a href="https://git-scm.com/">GitHub/Gitpod</a>: was used for writing up all the code.</li>
        <li><a href="https://www.figma.com/">Figma</a>: was used for the design layout of the website.</li>
        <li><a href="https://www.heroku.com/">Heroku</a>: was used for the deployment of the website.</li>
    </ul>
<h4>Testing</h4>
    <ul>
        <a href="https://en.wikipedia.org/wiki/Unit_testing">Unittest</a>: was used for the individual testing of each route.
    </ul>

<hr/>

<h3>Testing<h3>

<h4>Validation of Code</h4>

With the validation of the code using the following two validation sites. Using W3C validation all the HTML that was written was correct, but all the Flask
inputs come up with errors. As this is not part the HTML5 language. Using the W3C CSS validation for the CSS3 that was written, the result was No Errors Found.

<h4>Automated Testing</h4>

Created a test.py file to test each route that was created in the app.py file. The test.py file uses the unittest that runs each route, when the following 
is entered in a terminal python3 test.py. Once that is entered the unittest will run.

<h4>Manual Testing</h4>
<ol>
    <li>
        <h5>Responsive</h5>
        <ul>
            <li>
            Used Chrome dev tools and to test the responsiveness of the wed site. When resizing the screen from 4k screen, laptop, tablet and iphone
            and is responding correctly. Did test if the website will work on other browsers and loaded up correctly.
            </li>    
        </ul>
    </li>
    <li>
        <h5>Sign In</h5>
            <h6>Correct User details</h6>
            <ul>
                <li>
                Clicked on the Sign In link,
                Sign in page loaded up and entered in my username and password,
                The Sign in page will redirected to the Home page.
                </li>    
            </ul>
            <h6>Incorrect User details</h6>
            <ul>
                <li>
                Clicked on the Sign In link,
                Sign in page loaded up and entered in my username and incorrect password,
                The Sign In page prompt a message inform the user that their details are incorrect.
                The page will not redirect to any other page.
                </li>    
            </ul>
    </li>
    <li>
        <h5>Registration</h5>
            <h6>Correct User details</h6>
            <ul>
                <li>
                Clicked on the Registration link,
                Registration page loaded up and entered in my username and password,
                A confirmation password is required to compare passwords,
                The Registration page will redirected to the Home page.
                </li>    
            </ul>
            <h6>Incorrect User details</h6>
            <ul>
                <li>
                Clicked on the Registration link,
                Registration page loaded up and entered in my username and password,
                A confirmation password is required to compare passwords,
                If passwords does not match a message will prompt the user their passwrods does not match.
                The Registration page will not redirect to any other page.
                </li>    
            </ul>
    </li>
    <li>
        <h5>Add Recipe</h5>
            <ul>
                <li>
                Clicked on the Add recipe link,
                Add recipe page loaded up and allows you to enter the new recipe details,
                Submitted the from blank and the page does request you to fill in the from,
                Filled out the from and submitted the from,
                Add recipe page will redirect you to the display recipes page,
                Opened the recipe and the whole from was filled out.
                </li>    
            </ul>
    </li>
    <li>
        <h5>Edit Recipe</h5>
            <ul>
                <li>
                Clicked on the Edit recipe button,
                Edit recipe page loaded up and allows you to enter the new details to a recipe and the recipe is already populated,
                Filled out the from and submitted the from,
                Edit recipe page will redirect you to the display recipes page.
                Opened the recipe and the whole from was filled out.
                </li>    
            </ul>
    </li>
    <li>
        <h5>Delete Recipe</h5>
            <ul>
                <li>
                Clicked on the Delete recipe button,
                The recipe is deleted form the database,
                The Delete recipe page will redirect you to the display recipe page,
                A message will appear stating the recipe has been deleted.
                </li>    
            </ul>
    </li>
    <li>
        <h5>Sign Out</h5>
            <ul>
                <li>
                Clicked on the Sign out link,
                The Sign Out will redirect you to the Home page,
                A message will appear stating You have been Signed Out! Good Bye.
                </li>    
            </ul>
    </li> 
</ol>

<hr/>

<h4>Deployment</h4>
