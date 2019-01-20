


def lazy_encrypt(output, input, mapping_encrypt):
    input_file = open("/home/yuriipopovych/Learning/python/Objects-Algorithms/Exam/lazyEncrypt/{0}".format(input))
    output_file = open("/home/yuriipopovych/Learning/python/Objects-Algorithms/Exam/lazyEncrypt/{0}".format(output), "w")
    for line in input_file:
        for word in line:
            if word in mapping_encrypt:
                word = mapping_encrypt[word]
            output_file.write(word)
    input_file.close()
    output_file.close()
            
            

        




lazy_encrypt("anOutputFile.txt", "anInputFile.txt", {"e": "o", "o": "a"})
print("Done running! Check anOutputFile.txt for the result.")

