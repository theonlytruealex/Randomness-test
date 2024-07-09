import requests
from cairosvg import svg2png

def write_text(data: str, path: str):
    with open(path, 'w') as file:
        file.write(data)


# url = r"https://math.vercel.app/?from=\textbf{Result:}\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space\space%20p-\text{value}={1}"

# svg = requests.get(url).text

# write_text(svg, '../../assets/autocorr/temp/1.svg')

def gen_img(p_value, alpha):
    
    url = r"https://math.vercel.app/?from=\textbf{Result:}\space\space\space\space\space\space\space\space\space\space\space%20p-\text{value}="+str(p_value)
    svg = requests.get(url).text
    svg2png(bytestring=svg,write_to='../../assets/autocorr/temp/1.png')
    
    status = "accepted"
    if p_value <= alpha:
        status = "rejected"
    url = r"https://math.vercel.app/?from=\textbf{Conclusion:%20}\text{For%20a%20significance%20level%20of%20}\alpha=" + str(alpha) +r",%20\text{the%20}H_0\text{%20hypothesis%20is%20"+status+r".}" 
    svg = requests.get(url).text
    svg2png(bytestring=svg,write_to='../../assets/autocorr/temp/2.png')
    # write_text(svg, '../../assets/autocorr/temp/1.svg')

# gen_img(0.1, 0.9)