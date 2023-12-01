import { useAuth } from "@clerk/clerk-react";
import { UserButton } from "@clerk/clerk-react";
import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import { getData } from "../hooks/queries/get/getQueries";
import { useEffect, useState } from "react";
import { ProfileDto } from "../interfaces/ProfileDto";

export default function Dashboard() {
  const [userData, setUserData] = useState<ProfileDto>();
  const { userId, getToken } = useAuth();

  useEffect(() => {
    (async () => {
      try {
        const token = await getToken();
        if (userId && token && token.length > 0) {
          const data = await getData(token, userId);
          setUserData(data);
        }
      } catch (e) {
        console.error(e);
      }
    })();
  }, [getToken]);

  return(
    <Container maxWidth="lg">
      <Box sx={{ my: 4 }}>
        <Typography variant="h4" component="h1" gutterBottom>
          <>
          <UserButton />
          <div>Hello </div>
          <div>User Id : {userData?.id}</div>
          <div>User Email : {userData?.email}</div>
          <div>User Username : {userData?.username}</div>
          </>
        </Typography>
      </Box>
    </Container>
  );
}