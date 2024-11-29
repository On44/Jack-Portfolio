from flask import Flask, render_template, url_for

app = Flask(__name__)

# Home Page Route
@app.route('/')
def home():
    return render_template('index.html')

# About Page Route
@app.route('/about')
def about():
    return render_template('about.html')

# Contact Page Route
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Projects Page Route
@app.route('/projects')
def projects():
    # List of projects to pass dynamically to the projects page
    project_list = [
        {
            "title": "The Prime Boutique Shop",
            "description": "The primary aim of The Prime Boutique Shop is to create a reliable platform where users can explore, select, and purchase items without interruptions. By integrating modern technology like React and Mpesa, the system ensures efficiency, security, and an engaging user experience.",
            "link": "https://github.com/On44/prime-boutique-system01"
        },
        {
            "title": "BigSeller POS System",
            "description": "BigSeller POS System is a Point-of-Sale (POS) platform tailored for small to medium-sized businesses, especially eCommerce retailers and brick-and-mortar stores. It helps businesses streamline sales, inventory management, customer interactions, and financial reporting.",
            "link": "https://github.com/On44/BigSeller-POS"
        },
        {
            "title": "D&S Cloud Computing",
            "description": "D&S Cloud Computing is a tech-focused company based in Kenya, dedicated to delivering innovative technology solutions that empower businesses to thrive in the digital age. The company primarily specializes in Point of Sale (POS) systems and Enterprise Resource Planning (ERP) solutions, with a mission to simplify operations and drive efficiency for businesses across various industries.",
            "link": "https://github.com/On44/D-S-Cloud-Web-Page"
        },
        {
            "title": "Expense Tracker App",
            "description": "The Expense Tracker App is a mobile application built using React Native, designed to help users efficiently track and manage their expenses, gain insights into their spending habits, and achieve financial goals. It offers a seamless user experience with cross-platform compatibility for both Android and iOS devices.",
            "link": "https://github.com/yourusername/react-native-app"
        }
    ]
    return render_template('projects.html', projects=project_list)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
