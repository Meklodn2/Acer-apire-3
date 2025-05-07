def lonngestCommonPrefix(strs):
    if not strs:
        return ""

    prefix = strs[0] #birinchi so'zni prefiks deb olamiz
    for word in strs [1:]: #Listni ichidagi qolgan so'zlarni tekshiramiz
        while not word.startswith(prefix):#so'z prefiks bo'lmasa qiaqartirish
            prefix = prefix[:-1]#ohiridan bitta harif ayirish
            if not prefix:
                return ""
    return prefix
print(lonngestCommonPrefix(["flower","flow","flight"]))