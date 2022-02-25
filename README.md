<h1 align="center">Premier League Hall Of Fame</h1>

<h2 align="center"><img src="https://github.com/Elippsis007/Premier-League-HoF/blob/main/readme_images/Am_I_Responsive.png"></h2>

## Project Overview

This is The Premier League Hall Of Fame. A website where fans can view Premier League Hall Of Famers, purchase latest season jerseys and memorabilia.

## Deployed Site
[View the Premier League Hall Of Fame](https://premier-league-hof.herokuapp.com/)

## User Experience (UX)

-   ### User stories

<h2 align="center"><img src="https://github.com/Elippsis007/Premier-League-HoF/blob/main/readme_images/user_story/user_story.png"></h2>

-   ### Design

    -   #### Structure
    
        -   The structure of the website was purposely designed to maintain a fluid, consistent display throughout as to not look cluttered, easy to navigate and easy to find what you are looking for.
        
        -   Website Colors and Font: Website colors and font remain consistent throughout.
    
    -   #### Colour Scheme
    
        -   The color scheme on this website is based on the Premier League brand which is meant to reinforce the brand identity and I feel it's appealing and easy on the eye. 
        
       <h2 align="center"><img src="https://github.com/Elippsis007/Premier-League-HoF/blob/main/readme_images/website_design/color_scheme/pl_color_palette.png"></h2>
       
       <h2 align="center"><img src="https://github.com/Elippsis007/Premier-League-HoF/blob/main/readme_images/website_design/color_scheme/color-combo.png"></h2>
            
    -   #### Typography
    
        -   [Bebas Neue](https://fonts.google.com/specimen/Bebas+Neue?query=Bebas+Neue) is the main font used throughout the whole website with cursive as the fallback font in case for any reason the font isn't being recognized on different operating systems.
        
## Wireframes

-   Register Page Wireframe - [view](https://github.com/Elippsis007/Premier-League-HoF/blob/main/readme_images/website_design/wireframes/desktop_wireframes/register_signup.png)

-   Log In Page Wireframe - [view](https://github.com/Elippsis007/Premier-League-HoF/blob/main/readme_images/website_design/wireframes/desktop_wireframes/login_sign_in.png)

-   Logout Page Wireframe - [view](https://github.com/Elippsis007/Premier-League-HoF/blob/main/readme_images/website_design/wireframes/desktop_wireframes/log_out_sign_out.png)

-   Home Page Wireframe - [view](https://github.com/Elippsis007/Premier-League-HoF/blob/main/readme_images/website_design/wireframes/desktop_wireframes/home.png)

-   Hall Of Fame Page Wireframe - [view](https://github.com/Elippsis007/Premier-League-HoF/blob/main/readme_images/website_design/wireframes/desktop_wireframes/hall_of_fame.png)

-   All Products Page Wireframe - [view](https://github.com/Elippsis007/Premier-League-HoF/blob/main/readme_images/website_design/wireframes/desktop_wireframes/all_prod.png)

-   Checkout Page Wireframe - [view](https://github.com/Elippsis007/Premier-League-HoF/blob/main/readme_images/website_design/wireframes/desktop_wireframes/checkout.png)

-   Shopping Cart Page Wireframe - [view](https://github.com/Elippsis007/Premier-League-HoF/blob/main/readme_images/website_design/wireframes/desktop_wireframes/shopping_cart.png)

-   Order Summary Page Wireframe - [view](https://github.com/Elippsis007/Premier-League-HoF/blob/main/readme_images/website_design/wireframes/desktop_wireframes/order_summary.png)

-   Profile Page Wireframe - [view](https://github.com/Elippsis007/Premier-League-HoF/blob/main/readme_images/website_design/wireframes/desktop_wireframes/profile.png) 

-   Product Management Page Wireframe - [view](https://github.com/Elippsis007/Premier-League-HoF/blob/main/readme_images/website_design/wireframes/desktop_wireframes/product_management.png)

-   Product Management Page Wireframe - [view](https://github.com/Elippsis007/Premier-League-HoF/blob/main/readme_images/website_design/wireframes/desktop_wireframes/verify_email_message.png)

## Mobile Wireframes

-   Register/Login Page Wireframe - [view]()

-   Home Page Collapsible Wireframe - [view]()

-   User Page Wireframe - [view]() 

-   Add Book Page Wireframe - [view]()

-   Manage Genres - [view]()

## Features

<h2 align="center"><img src="https://github.com/Elippsis007/Premier-League-HoF/blob/main/readme_images/website_design/site_navigation/site_nav.png"></h2>

-   ### View Features - [view](https://github.com/Elippsis007/Premier-League-HoF/blob/main/FEATURES.md)

-   ### Features Implemented

    -   #### Register for profile
        - Create a profile to save their orders and personal information
        - Confirm their details are correct via email verification

    -   #### Logging into user profile
        - Log in to profile to see their orders and their personal information
        - Ability to edit personal information

    -   #### Product (Jerseys/Memorabilia) Pages
        - See the products for sale on the site
        - Sort products by A-Z, Name, Category, Price
        - Users can see the cost of the product
        - Product rating are also available to users.

    -   #### Product (Jerseys/Memorabilia) Detail Pages
        - See the products summary
        - Ability to select sizes and quanties required
        - Add to cart function        

    -   #### Products Management
        - Add product
        - Delete product
        - Edit product
        - Add product image

    -   #### Shopping Cart
        - Ability to change the number of products they wish to purchase
        - Breakdown of total costs

    -   #### Checkout
        - Ability to update and save their details for future purchases

-   ### Defensive Programming
    -  An error is launched if the user attempts to visit a part of the site where they are not authorised.
    -  When a product is added without the image a default image is added.
    -  There is form validation to all forms to make sure that all required information is included before submitting.
    -  If the user inputs wrong data they will be met with a popup explaining to them on how to continue.
    -  Any visitor that attempts to access a part of the website will be met with an error telling them that they are not authortised to access.
    -  @login_required decorator was added to restrict users trying to access certain pages not available to them.
    -   A logged out user tries to access a restricted page, they will be redirected to the login page.
       
-   ### Future Features
    - The ability for users to add reviews to products.
    - A new range of products
    - Video embedded on the HOF page for each footballer
    - A voting page for the next inductee to hall of fame.

## Database
The database uses SQL through PostgreSQL and was created using fixtures with categories.json, products.json and hof.json

<h2 align="center"><img src="https://github.com/Elippsis007/Premier-League-HoF/blob/main/readme_images/website_design/db_schema/db_schema_hof.png"></h2>

-   ### [SQLite](https://www.sqlite.org/index.html)
    - A cloud database that holds the products, user and order fields.
-   ### [Postgres](https://www.postgresql.org/) 

## Sitemap
-   The sitemap was created using [Octopus](https://octopus.do/)
-   The sitemap can be found [Here](https://github.com/Elippsis007/Premier-League-HoF/blob/main/readme_images/website_design/sitemap/hof_sitemap.png)

## Technologies Used

### Frameworks, Libraries & Programs Used
1.  [Django:](https://www.djangoproject.com/)
     - Django was used as the main python framework in the building of this project.
1.  [Heroku:](https://www.heroku.com/)
     - Heroku was used as a cloud based platform to deploy this site.
1.  [JSON:]https://www.json.org/json-en.html)
     - MongoDB Atlas was used as the database for the creation of this project.
1.  [Jinja:](https://jinja.palletsprojects.com/en/3.0.x/)
     - Jinja was used for templating.
1.  [Freeformatter-Css beautifier:](https://www.freeformatter.com/css-beautifier.html)
     - This was used to format the CSS stylesheet.
1.  [Freeformatter-Html beautifier:](https://www.freeformatter.com/html-formatter.html)
2.  - This was used to format the HTML accross the website.
3.  [JSON formatter-JSON beautifier:](https://jsonformatter.org/)
     - This was used to format each .JSON files.
4.  [Font Awesome:](https://fontawesome.com/)
     - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
5.  [BootStrap:](https://getbootstrap.com/)
     - Various aspects of this website were structured using Bootstrap.
     - Bootstrap was used to make some of this website responsive.
6.  [BULMA:](https://bulma.io/)
     - Some aspects of this website were also structured using BULMA.
     - BULMA was used for CSS and to make some of this website responsive.
7.  [CSS Tricks:](https://css-tricks.com/)
     - This was used as a general reference resource.
8.  [Balsamiq:](https://balsamiq.com/)
     - Balsamiq was used to create the [wireframes]() during the design process.
9.  [Google DevTools:](https://developer.chrome.com/docs/devtools/)
     - Google Dev Tools was used throughout the project for various styling and testing purposes.
10.  [Coolors:](https://coolors.co/)
     - Coolors.co was used to create the project's color palette.
11.  [Git](https://git-scm.com/)
     - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
12.  [GitHub:](https://github.com/)
     - GitHub is used to store the project's  code after being pushed from Git.
13.  [StackOverflow:](https://stackoverflow.com/)
     - Stack Overflow was used as a general reference resource.
14.  [Responsive Design Checker:](http://ami.responsivedesign.is/#)
     - Used to check website response across device types.

### Testing
Testing information can be found here in the separate [TESTING.md]()

## Deployment

This project was developed using Gitpod IDE and pushed to Github using the in-built terminal. Github can only host static websites it was necessary to deploy this project to Heroku because it is a compatible hosting platform for a back-end focused websits like this one.

This project was deployed using Heroku and stored in GitHub.

Before deploying the website to Heroku, the following three must be followed to allow the app to work in Heroku:

1. Create requirements.txt file that contains the names of packages being used in Python. It is important to update this file if other packages or modules are installed during project development by using the following command:
    - pip freeze --local > requirements.txt

2. Create Procfile that contains the name of the application file so that Heroku knows what to run. If the Procfile has a blank line when it is created remove this as this may cause problems.

3. Then push these files to GitHub. Once those steps are done, the website can be deployed in Heroku.

### Heroku Deployment:

    1. Log into Heroku.
    2. Click the New button.
    3. Click the option to create a new app.
    4. Enter the app name in lowercase letters.
    5. Select the correct geographical region.

### Setting the environment variables:

Navigate to the settings tab and then click the Reveal Config Vars button and add the following:

    {TEXT TO GO HERE}
    
### Enable automatic deployment:

    1. Click the Deploy tab
    2. In the Automatic deploys section, choose the branch you want to deploy from then click Enable Automation Deploys.

### Connect app to Github Repository
    1. Click the deploy tab and connect to GitHub.
    2. Type the name of the repository into the search bar presented.
    3. Click the Code dropdown button next to the green Gitpod button.
    4. When the correct repository displays click the connect button.

### Making a clone to run locally

It is important to note that this project will not run locally unless an env.py file has been set up by the user which contains the IP, PORT, MONGO_DBNAME, MONGO_URI and SECRET_KEY which have all been kept secret in keeping with best security practices.

    1. Log into GitHub.
    2. Select the respository.
    3. Click the Code dropdown button next to the green Gitpod button.
    4. Download ZIP file and unpackage locally and open with IDE. Alternatively copy the URL in the HTTPS box.
    5. Open the alternative editor and terminal window.
    6. Type 'git clone' and paste the copied URL.
    7. Press Enter. A local clone will be created.
    
Once the project been loaded into the IDE it is necessary to install the necessary requirements which can be done by typing the following command.

-   -pip install -r requirements.txt

### How to Fork the respository.
    1. Log into GitHub.
    2. In Github go to (https://github.com/Elippsis007/Premier-League-HoF).
    3. In the top right hand corner click "Fork".

## Credits

### Design and research

#### The following is what I have used for reference and inspiration:
    
### Technical

-   [Bootstrap:](https://getbootstrap.com/): Bootstrap was used throughout the project mainly to make the site responsive using the Bootstrap Grid System.
1.  [Font Awesome:](https://fontawesome.com/)
     - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
1.  [w3Schools:](https://www.w3schools.com//)
     - For checking proper syntax of HTML and CSS elements.
1.  [W3C Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
     - For checking markup validity of HTML.
1.  [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
     - For checking CSS styling validity.
1.  [Stackoverflow](https://stackoverflow.com/)
     - I used Stackoverflow to help me with issues I was having when it was styling, margins, centering a div.

### Content

-   All content was written by the developer.

### Media

****

### Acknowledgements

-   My mentor Gerry for continuous helpful feedback and support.

-   Tutor support at Code Institute for their support.

-   I'd like to thank my girlfriend, mates and family for testing the website on their devices and for suggesting changes and bugs.

## References

Fontawesome: https://www.fontawesome.com
