for (let i = 0; i < document.querySelectorAll(".jmeno").length; i++) {
    let url = document.querySelectorAll(".jmeno a")[i].getAttribute("href");
    let name = document.querySelectorAll(".jmeno")[i].innerText;
    setTimeout(() => {
        downloadDataUrlFromJavascript(name, url);
    }, i * 200);
}

function downloadDataUrlFromJavascript(filename, dataUrl) {
    // Construct the 'a' element
    var link = document.createElement("a");
    link.download = filename;
    link.target = "_blank";

    // Construct the URI
    link.href = dataUrl;
    document.body.appendChild(link);
    link.click();

    // Cleanup the DOM
    document.body.removeChild(link);
    delete link;
}