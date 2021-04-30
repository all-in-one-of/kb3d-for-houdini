string kit = detail(0, "kit", 0);
string path = s@path;
//path = re_replace(" ", "_", path);

// --- PATH EXCEPTIONS ------------------------
if (kit == "Greebles") {
    path = join(split(path, "/")[1:], "/");
}
// --------------------------------------------

// --- SCALE EXCEPTIONS -----------
float scale = 1.0;
if (kit == "Wasteland" || 
    kit == "SecretLab" ||
    kit == "StoreFronts")
{
    scale = 0.01;
}
setdetailattrib(0, "scale", scale);
// --------------------------------

string matnet = chs('../matnet');
s@shop_materialpath = concat ( matnet, '/', s@shop_materialpath );

if (kit != "KitBash3D") {
    s@name = split(path, "/")[0];
}
else {
    s@name = split(path, "/")[-1];
}

s@path = "/" + kit + "/" + path;

