import { API_PATHS, BASE_URL } from "../../../utils/ApiPaths";
import { ProfileDto } from "../../../interfaces/ProfileDto";

export const getData = async (token: string, id: string) => {
  const response = await fetch(BASE_URL + "/" + API_PATHS.PROFILE + "/" + id, {
    headers: {
      Authorization: `Bearer ${token}`,
      ContentType: 'application/json',
    },
  });
  const data: Promise<ProfileDto> = response.json();
  return data
}