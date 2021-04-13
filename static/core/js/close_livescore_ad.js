var bannerAd, footerAd;
var remover = setInterval(function () {
    bannerAd = $('#wff_floating_banner_container_FWE5270232E20FA0DB');
    footerAd = $('div.wff_link_container');
    if (bannerAd.length > 0 && footerAd.length > 0) {
        bannerAd.remove();
        footerAd.remove();
        clearInterval(remover);
    }
}, 500);