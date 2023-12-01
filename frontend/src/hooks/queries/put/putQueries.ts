import { API_PATHS } from "../../../utils/ApiPaths";
import { TestDto } from "../../../interfaces/ProfileDto";
import usePut from "./usePut";

export const useUpdateData = (id: string | undefined) =>
  usePut<TestDto>(API_PATHS.DATA + id);

