import argparse
python translate.py -gpu 0  -batch_size 1  -beam_size 5  -model summary/gigaword_copy_acc_51.78_ppl_11.71_e20.pt  -src ./test.txt  -share_vocab  -output data/giga/test_1.pred  -min_length 6  -verbose  -stepwise_penalty  -coverage_penalty summary  -beta 5  -length_penalty wu  -alpha 0.9  -block_ngram_repeat 3  -ignore_when_blocking "."



def summarize(input_file):
    parser = argparse.ArgumentParser(description='Processing Args')
    
