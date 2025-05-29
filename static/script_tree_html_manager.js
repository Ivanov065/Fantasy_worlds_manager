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
    },
    addSameLevel: function(target) {
      let ulElm = target.closest("ul");
      let sameLevelCodeASCII = target
        .closest("[data-level]")
        .attr("data-level")
        .charCodeAt(0);
      ulElm.append(jQuery("#levelMarkup").html());
      ulElm
        .children("li:last-child")
        .find("[data-level]")
        .attr("data-level", String.fromCharCode(sameLevelCodeASCII));
    },
    addSubLevel: function(target) {
      let liElm = target.closest("li");
      let nextLevelCodeASCII = liElm.find("[data-level]").attr("data-level").charCodeAt(0) + 1;
      liElm.children("ul").append(jQuery("#levelMarkup").html());
      liElm.children("ul").find("[data-level]")
        .attr("data-level", String.fromCharCode(nextLevelCodeASCII));
    },
    removeLevel: function(target) {
      target.closest("li").remove();
      
    }
  };

  // Treeview Functions
  jQuery(".js-treeview").on("click", ".level-add", function() {
    jQuery(this).find("span").toggleClass("fa-plus").toggleClass("fa-times text-danger");
    jQuery(this).siblings().toggleClass("in");
  });

  // Add same level
  jQuery(".js-treeview").on("click", ".level-same", function() {
    treeview.addSameLevel(jQuery(this));
    treeview.resetBtnToggle();
  });

  // Add sub level
  jQuery(".js-treeview").on("click", ".level-sub", function() {
    treeview.addSubLevel(jQuery(this));
    treeview.resetBtnToggle();
  });
    // Remove Level
  jQuery(".js-treeview").on("click", ".level-remove", function() {
    treeview.removeLevel(jQuery(this));
  }); 

  // Selected Level
  jQuery(".js-treeview").on("click", ".level-title", function() {
    let isSelected = jQuery(this).closest("[data-level]").hasClass("selected");
    !isSelected && jQuery(this).closest(".js-treeview").find("[data-level]").removeClass("selected");
    jQuery(this).closest("[data-level]").toggleClass("selected");
  }); 
});
