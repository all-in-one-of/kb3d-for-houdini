string fbxpath  = chs('fbx_path');
string allkitnames = chs("all_kit_names");
string allkits[] = split(allkitnames, " ");
string kit;

foreach (string k; allkits)
{
    string pattern = "*" + k + "*";
    if (match(pattern, fbxpath))
    {
        kit = k;
        break;
    }
    else
    {
        kit = "KitBash3D";
    }
}

s@kit = kit;