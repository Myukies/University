<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Set Session</title>
</head>
<body>
    <form action="setSession.jsp" method="post">
        Enter User Name: <input type="text" name="username">
        <input type="submit" value="Submit">
    </form>

    <%
        String userName = request.getParameter("username");
        if (userName != null && !userName.isEmpty()) {
            session.setAttribute("username", userName);
            out.println("User Name stored in session variable successfully.");
        }
    %>
</body>
</html>
