import streamlit as st
import math

resultado = 0

st.title('Calculadora padrão')

n1 = st.number_input('Valor 1: ')
n2 = st.number_input('Valor 2: ')

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("Somar"):
        resultado = n1 + n2
        resultado = f"{resultado:,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")
        st.success(f'A soma é: {resultado}')
        
        # 3. Insira o botão de somar especificamente na col1
with col2:
    if st.button("Subtrair"):
        resultado = n1 - n2
        resultado = f"{resultado:,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")
        st.success(f'A subtração é: {resultado}')
        
with col3:
    if st.button("Multiplicar"):
        resultado = n1 * n2
        resultado = f"{resultado:,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")
        st.success(f'A multiplicação é: {resultado}')
        
with col4:
    if st.button("Dividir"):
        resultado = n1 / n2
        resultado = f"{resultado:,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")
        st.success(f'A divisão é R$: {resultado}')
        
with col5:
    if st.button("Raiz quadrada"):
        raiz = math.sqrt(n1)
        n1 = f"{n1:,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")
        raiz = f"{raiz:,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")
        st.success(f'A raíz quadrada de {n1} é: {raiz}')