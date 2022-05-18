import NextAuth from "next-auth";
import CredentialsProvider from "next-auth/providers/credentials";

export default NextAuth({
  providers: [
    CredentialsProvider({
      id: "credentials",
      name: "credentials",
      credentials: {
        email: {
          label: "email",
          type: "email",
        },
        password: { label: "Password", type: "password" },
      },
      async authorize(credentials, req) {
        const payload = {
          email: credentials.email,
          password: credentials.password,
        };

        const res = await fetch("http://localhost:8001/api/users/login", {
          method: "POST",
          body: JSON.stringify(payload),
          headers: {
            "Content-Type": "application/json",
            tenant: credentials.tenantKey,
            "Accept-Language": "en-US",
          },
        });

        const user = await res.json();
        if (!res.ok) {
          throw new Error(user.exception);
        }
        // If no error and we have user data, return it
        if (res.ok && user) {
          return user;
        }

        // Return null if user data could not be retrieved
        return null;
      },
    }),
  ],
  secret: process.env.JWT_SECRET,
  pages: {
    signIn: "/login",
  },
  callbacks: {
    async jwt({ token, user, account }) {
      if (account && user) {
        return {
          ...token,
          accessToken: user.data.token,
          refreshToken: user.data.refreshToken,
        };
      }

      return token;
    },

    async session({ session, token }) {
      session.user.accessToken = token.accessToken;
      session.user.refreshToken = token.refreshToken;
      session.user.accessTokenExpires = token.accessTokenExpires;

      return session;
    },
  },
  // Enable debug messages in the console if you are having problems
  debug: process.env.NODE_ENV === "development",
});
// import NextAuth from "next-auth";
// import CredentialsProvider from "next-auth/providers/credentials";

// export default NextAuth({
//   providers: [
//     CredentialsProvider({
//       id: "credentials",
//       name: "credentials",
//       authorize: async (credentials) => {
//         try {
//           const user = await axios.post(
//             "http://localhost:8002/users",
//             {
//               user: {
//                 email: credentials.email,
//                 password: credentials.password,
//               },
//             },
//             {
//               headers: {
//                 accept: "*/*",
//                 "Content-Type": "application/json",
//               },
//             }
//           );

//           if (user) {
//             return { status: "success", data: user };
//           }
//         } catch (e) {
//           const errorMessage = e.response.data.message;
//           // Redirecting to the login page with error message          in the URL
//           throw new Error(errorMessage + "&email=" + credentials.email);
//         }
//       },
//     }),
//   ],
//   callbacks: {
//     async jwt(token, user) {
//       if (user) {
//         token.accessToken = user.data.token;
//       }

//       return token;
//     },

//     async session(session, token) {
//       session.accessToken = token.accessToken;
//       return session;
//     },
//   },
//   options: {
//     providers,
//     callbacks,
//     pages: {
//       error: "/login", // Changing the error redirect page to our custom login page
//     },
//   },
// });
