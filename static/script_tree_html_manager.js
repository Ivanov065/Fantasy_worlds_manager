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

  // Selected Level
  // jQuery(".js-treeview").on("click", ".level-title", function() {
  //   let isSelected = jQuery(this).closest("[data-level]").hasClass("selected");
  //   !isSelected && jQuery(this).closest(".js-treeview").find("[data-level]").removeClass("selected");
  //   jQuery(this).closest("[data-level]").toggleClass("selected");
  // }); 
});
