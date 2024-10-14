import axios from "axios";

const BASE_URL = "http://127.0.0.1:5000/api"; // Substitua pelo seu endpoint real

// Função para pegar todas as URLs
export const getUrls = async () => {
  try {
    const response = await axios.get(`${BASE_URL}/urls`);
    console.log(response.data);
    return response.data.data; // Retorna a lista de URLs
  } catch (error) {
    console.error("Erro ao obter URLs:", error);
    throw error;
  }
};

export const getUrlById = async (id) => {
  try {
    const response = await axios.get(`${BASE_URL}/url/${id}`);
    console.log(response.data);
    return response.data.data; // Retorna uma URLs
  } catch (error) {
    console.error("Erro ao obter URLs:", error);
    throw error;
  }
};

// Função para adicionar uma nova URL
export const addUrl = async (url) => {
  try {
    const response = await axios.post(`${BASE_URL}/url`, { url });
    console.log(response.data);
    return response.data.data; // Retorna a URL adicionada
  } catch (error) {
    console.error("Erro ao adicionar URL:", error);
    throw error;
  }
};

// Função para deletar uma URL
export const deleteUrl = async (id) => {
  try {
    const response = await axios.delete(`${BASE_URL}/url/${id}`);
    return response.data; // Retorna o resultado da deleção
  } catch (error) {
    console.error("Erro ao deletar URL:", error);
    throw error;
  }
};
