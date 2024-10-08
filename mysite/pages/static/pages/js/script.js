// scroll_effect
$(document).ready(function () {
    // 要素の取得
    var scrollAnimationElm = document.querySelectorAll('.scroll_up, .scroll_left, .scroll_right, .animate');

    // アニメーションを実行する関数
    var scrollAnimationFunc = function () {
        for (var i = 0; i < scrollAnimationElm.length; i++) {
            var triggerMargin = 100;
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
