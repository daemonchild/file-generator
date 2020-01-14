function download_url()
{
    // Download file from a URL

    console.log (document.getElementById('urlstore').value)
    var link = document.createElement("a");
    link.href = document.getElementById('urlstore').value;
    link.click();

}

function send_email ()
{

    alert ("Email Feature is Under Construction")

}

function redirect()
{
    // Generates a new UID to avoid caching
    window.location.replace("/webapp");

}

// Borrowed code from: https://www.dyn-web.com/tutorials/forms/select/selected.php
function getSelectedOption(sel) {
    var opt;
    for ( var i = 0, len = sel.options.length; i < len; i++ ) {
        opt = sel.options[i];
        if ( opt.selected === true ) {
            break;
        }
    }
    return opt;
}


function rebuild_url() {


    var doc_type = (getSelectedOption(document.getElementById('select_doctype')).value);
    var compress_type = (getSelectedOption(document.getElementById('select_compress')).value);

    // build URL
    doc_url = '/fetch/' + doc_type

    if (compress_type !== "None") {

        url = doc_url + "?compress=" + compress_type
    } else {
        url = doc_url
    }

    document.getElementById('urlstore').value = url

}