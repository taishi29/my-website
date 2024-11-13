/* scroll_effect */
// getBoundingClientRect().top：要素の上端がビューポートの上端からどれくらいの距離にあるか。
// window.innerHeight：ビューポートの高さを取得。
$(document).ready(function () {
    // 要素の取得
    var scrollAnimationElm = document.querySelectorAll('.scroll_up, .scroll_left, .scroll_right, .animate');

    // アニメーションを実行する関数
    var scrollAnimationFunc = function () {
        for (var i = 0; i < scrollAnimationElm.length; i++) {
            var triggerMargin = 300;
            if (window.innerHeight > scrollAnimationElm[i].getBoundingClientRect().top + triggerMargin) {
                scrollAnimationElm[i].classList.add('on');
            }
        }
    };

    // ページが読み込まれた時点でアニメーションを実行
    scrollAnimationFunc();

    // スクロール時にもアニメーションを実行
    $(window).on('scroll', scrollAnimationFunc);
});


$(document).ready(function () {
    // 要素の取得
    var scrollAnimationElm = document.querySelectorAll('.extinction');
    var englishMessageElm = $('.appearance');

    var scrollAnimationFunc = function () {
        for (var i = 0; i < scrollAnimationElm.length; i++) {
            var triggerMargin = 625;

            // 要素がビューポート内に入ったときの処理
            if (window.innerHeight > scrollAnimationElm[i].getBoundingClientRect().top + triggerMargin) {
                scrollAnimationElm[i].classList.add('on');

                // 英語のメッセージを表示
                englishMessageElm.removeClass('hidden').addClass('visible');
            } else {
                // 要素がビューポート外に出たときの処理
                scrollAnimationElm[i].classList.remove('on');

                // 英語のメッセージを非表示
                englishMessageElm.removeClass('visible').addClass('hidden');
            }
        }
    };

    // ページが読み込まれた時点でアニメーションを実行
    scrollAnimationFunc();

    // スクロール時にもアニメーションを実行
    $(window).on('scroll', scrollAnimationFunc);
});

$(document).ready(function(){
    var zindex = 10;
    
    $("li.card7").click(function(e){
      e.preventDefault();
  
      var isShowing = false;
  
      if ($(this).hasClass("show")) {
        isShowing = true
      }
  
      if ($("ul.cards7").hasClass("showing")) {
        $("li.card7.show")
          .removeClass("show");
  
        if (isShowing) {
          $("ul.cards7")
            .removeClass("showing");
        } else {
          $(this)
            .css({zIndex: zindex})
            .addClass("show");
  
        }
  
        zindex++;
  
      } else {
        // no cards in view
        $("ul.cards7")
          .addClass("showing");
        $(this)
          .css({zIndex:zindex})
          .addClass("show");
        zindex++;
      }
      
    });
  });