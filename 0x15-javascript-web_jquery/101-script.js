window.onload = function () {
  const $myL = $('UL.my_list');

  $('DIV#add_item').click(() => {
    $myL.append('<li>Item</li>');
  });

  $('DIV#remove_item').click(() => {
    const thelastItem = $('UL.my_list LI').last();
    thelastItem.remove();
  });

  $('DIV#clear_list').click(() => {
    $myL.empty();
  });
};
