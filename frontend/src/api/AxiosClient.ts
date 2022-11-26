import axios, {AxiosRequestConfig} from "axios";
import {API_URL} from "../config";

const axiosConfig: AxiosRequestConfig = {
  // https://axios-http.com/docs/req_config
  headers: {'Content-Type': 'application/json'},
  baseURL: API_URL
};

const AxiosClient = axios.create(axiosConfig);

AxiosClient.interceptors.request.use(
  // Add your request interceptor here, e.g. if you need to automatically refresh token
  // or add some headers on each request
  // https://axios-http.com/docs/interceptors
  (config) => config,
  (error) => Promise.reject(error)
);

export default AxiosClient;
