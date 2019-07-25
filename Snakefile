rule all:
        input: ["results/mnist_model_results_summary.txt", "results/fashion_model_results_summary.txt", "results/mnist_results_summary_plots.pdf","results/fashion_results_summary_plots.pdf", "results/fashion.html", "results/mnist.html"]

rule fashion:
        input: "data/fashion.txt"
        output: "results/fashion_model_results_summary.txt","results/fashion_results_summary_plots.pdf", "results/fashion.html"
        message: "fashion: input={input}, output={output}"
        shell: '''python run_main.py {input} > {output}; mv fashion_results_summary_plots.pdf fashion_model_results_summary.txt fashion.html results'''

rule mnist:
        input: "data/mnist.txt"
        output: "results/mnist_model_results_summary.txt","results/mnist_results_summary_plots.pdf", "results/mnist.html"
        shell: '''python run_main.py {input} > {output}; mv mnist_results_summary_plots.pdf mnist_model_results_summary.txt mnist.html results/'''

rule copy:
        input: ["results/mnist_model_results_summary.txt", "results/fashion_model_results_summary.txt", "results/mnist_results_summary_plots.pdf","results/fashion_results_summary_plots.pdf", "results/fashion.html", "results/mnist.html"]
        shell: '''cp results/* /home/jovyan/results/'''


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
    
