// // Get references to the cart and checkout button
// var cart = document.getElementById("cart");
// var checkoutBtn = document.getElementById("checkoutBtn");

// // Check cart contents and show/hide checkout button
// function checkCart() {
//   if (cart.children.length > 0) {
//     // If cart has items, show the checkout button
//     checkoutBtn.style.display = "block";
//   } else {
//     // If cart is empty, hide the checkout button
//     checkoutBtn.style.display = "none";
//   }
// }

// // Call checkCart initially to set the button state
// checkCart();

// // Example: Adding items to the cart
// // You can customize this code to add items to the cart as per your requirements
// function addToCart(product) {
//   var item = document.createElement("div");
//   item.textContent = product;
//   cart.appendChild(item);
//   checkCart(); // Call checkCart after adding items to update the button state
// }

// // Example: Removing items from the cart
// // You can customize this code to remove items from the cart as per your requirements
// function removeFromCart(item) {
//   cart.removeChild(item);
//   checkCart(); // Call checkCart after removing items to update the button state
// }
