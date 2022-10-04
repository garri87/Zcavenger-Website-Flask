
    const header = document.createElement("header");
   
    header.setAttribute("class", "navigation");
    
    const logo = document.createElement("img");
    logo.setAttribute("src","Img/TitleTransparent.png");
    logo.setAttribute("id", "logo");

    const nav = document.createElement("nav");
    const home = createNavLink("Home");
    const development = createNavLink("Development");
    const contact = createNavLink("Contact");
    const download = createNavLink("DOWNLOAD");

    home.setAttribute("href", "index.html");
    development.setAttribute("href", "Development.html");
    contact.setAttribute("href", "Index.html#form");
    download.setAttribute("href", "https://garri87.itch.io/zcavenger/download/eyJpZCI6MTI5NDQ1MiwiZXhwaXJlcyI6MTY2MjEyODcxMH0%3d.V1gBg9hIQMlWcqx3APjQ8x%2f4RjM%3d")
    
    home.setAttribute("id","navigationButton");
    development.setAttribute("id", "navigationButton");
    contact.setAttribute("id","navigationButton");
    download.setAttribute("class", "downloadButton");


    document.body.appendChild(header);
    header.appendChild(logo);
    header.appendChild(nav);
    nav.appendChild(home);
    nav.appendChild(development);
    nav.appendChild(contact);
    nav.appendChild(download);

function createNavLink(title) {

    const link = document.createElement("a");
    link.innerHTML = title;
    return link;
}
