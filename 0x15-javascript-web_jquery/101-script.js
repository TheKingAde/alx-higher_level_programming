// Wait for the document to be ready
$(document).ready(function () {
  // Add item: When the user clicks on DIV#add_item
  $('#add_item').click(function () {
    const newItem = $('<li>').text('Item'); // Create a new <li> element with the text "Item"
    $('ul.my_list').append(newItem); // Append the new <li> element to UL.my_list
  });

  // Remove item: When the user clicks on DIV#remove_item
  $('#remove_item').click(function () {
    $('ul.my_list li:last-child').remove(); // Remove the last <li> element from UL.my_list
  });

  // Clear list: When the user clicks on DIV#clear_list
  $('#clear_list').click(function () {
    $('ul.my_list').empty(); // Remove all elements from UL.my_list
  });
});
