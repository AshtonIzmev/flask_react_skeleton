import { API_PATHS } from "../../../utils/ApiPaths";
import { TestDto } from "../../../interfaces/ProfileDto";
import usePost from "./usePost";

export const useCreateData = () =>
  usePost<TestDto>(API_PATHS.DATA);
