import {AxiosResponse} from "axios";

export type Response<TData, TConfig = any> = AxiosResponse<TData, TConfig>;

export type PaginatedResponseData<TData> = {
  count: number;
  previous: string | null,
  next: string | null,
  results: TData[]
}
