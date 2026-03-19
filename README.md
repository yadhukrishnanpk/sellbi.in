# Sellbi.in | E-Commerce for Creators 🎨

**Sellbi.in** is a full-stack e-commerce platform designed specifically for artists, crafters, and makers. It provides a dedicated space for creators to showcase their unique work—from handmade treasures to canvas paintings—and connect directly with buyers who value authentic, homemade products.

---
## 🚀 Features

* **Creator Showcases:** High-quality product grids for displaying artwork and crafts.
* **Dynamic Cart System:** Real-time cart updates and subtotal calculations.
* **Secure Authentication:** User login and signup functionality for a personalized experience.
* **Responsive UI:** A modern, dark-themed interface built with a focus on custom CSS Grid and Flexbox layouts.
* **Product Management:** Backend integration for handling product details, pricing, and descriptions.
---
## 🛠️ Tech Stack

* **Backend:** Python, Django
* **Frontend:** HTML5, CSS3 (Custom Modular Stylesheets)
* **Database:** SQLite3
* **Design:** Custom UI with Google Fonts (Bricolage Grotesquel) and FontAwesome Icons
---
## 📂 Project Structure

```
├── core/               # Django project settings
├── products/           # Product listings and detail logic
├── cart/               # Shopping cart functionality
├── static/
│   ├── css/            # Isolated stylesheets (login.css, products.css, cart.css, etc.)
└── templates/          # Responsive HTML layouts and Django Template inheritance 
```
---

## 🛠️ Advanced Implementation

### Technical Highlights
* **DRY Architecture:** Leveraged Django's template inheritance to maintain a single source of truth for the UI layout.
* **Modular CSS:** Engineered isolated stylesheets for each view (Cart, Login, Products) to eliminate style bleeding and improve maintainability.
* **Efficient ORM Queries:** Optimized backend logic to fetch product details and calculate cart totals with minimal database hits.

### Design Principles
* **User-Centric Navigation:** A fixed, blur-effect navigation bar provides constant access to the Cart and About sections.
* **Visual Hierarchy:** Used font weighting and contrast to ensure product prices and "Add to Cart" actions are the primary focus for users.

---

## 🚀 Upcoming Enhancements
- [ ] **Payment Gateway:** Integration of Razorpay for live transactions.
- [ ] **Search Optimization:** Adding a search bar with cubic-bezier animated transitions.
- [ ] **User Profiles:** Expanded profiles for creators to share their artistic journey.


---

> [!IMPORTANT]
> Educational Purpose
>  **Disclaimer:** This project, **Sellbi.in**, was developed for **educational and portfolio purposes** as part of a full-stack web development showcase.
