import challenge3 as c3
from tqdm import tqdm


if __name__ == '__main__':

        with open('data/4.txt', 'r') as f:
                input_hex = f.read().splitlines()

        score = []
        chars = []
        for cypher in tqdm(input_hex):
                
                prob_char, sc = c3.check_all_chars(cypher)
                score.append(sc)
                chars.append(prob_char)


        index = score.index(max(score))
        
        print("The input hex:\n" + input_hex[index]+ 
                "\n has likely been XOR'ed with '%s'"%chars[index] +
                "\n to give the sentence:\n" +
                c3.xor_hx_char(input_hex[index], chars[index]).decode('ascii')) 

