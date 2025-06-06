jQuery(function() {
  let treeview = {
    resetBtnToggle: function() {
      jQuery(".js-treeview")
        .find(".level-add")
        .find("span")
        .removeClass()
        .addClass("fa fa-plus");
      jQuery(".js-treeview")
        .find(".level-add")
        .siblings()
        .removeClass("in");
    }
  };

  // Treeview Functions
  jQuery(".js-treeview").on("click", ".level-add", function() {
    jQuery(this).find("span").toggleClass("fa-plus").toggleClass("fa-times text-danger");
    jQuery(this).siblings().toggleClass("in");
  });
});
