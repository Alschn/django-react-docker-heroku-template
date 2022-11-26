import AxiosClient from "./AxiosClient";
import {Response} from "./types";

interface ResponseBody {
  text: string;
}

export const getUppercaseText = (text: string): Promise<Response<ResponseBody>> => {
  return AxiosClient.get(`/api/test?text=${text}`);
};
