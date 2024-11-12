func mergeAlternately(word1 string, word2 string) string {
    word1_slice := strings.Split(word1, "")
    word2_slice := strings.Split(word2, "")
    merged := ""
    i := 0

    for (len(merged) < len(word1) + len(word2)) {
        if (len(word1_slice) > i) {
            merged += word1_slice[i]
        }

        if (len(word2_slice) > i) {
            merged += word2_slice[i]
        }

        i++
    }

    return merged
}