/*
 * SWAMI KARUPPASWAMI THUNNAI
 * 
 * @author VISWESWARAN NAGASIVAM
 */

package api.auth;

import api.global.SensibleGlobal;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.JLabel;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;
import org.jsoup.Connection;
import org.jsoup.Connection.Method;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import sensible.client.CRM;

/**
 *
 * @author Visweswaran
 */
public class RestLogin{
    
    private final String phone;
    private final String password;
    private final JLabel status;
    
    /**
     * Constructor for initializing the private variables
     * @param phone The phone number of the user.
     * @param password The password of the user.
     */
    public RestLogin(String phone, String password, JLabel status) {
        this.phone = phone;
        this.password = password;
        this.status = status;
    }
    
    public void login()
    {
        status.setText("LOGGING IN...");
        try 
        {
            JSONObject json = new JSONObject();
            json.put("phone", this.phone);
            json.put("password", this.password);
            Document document = Jsoup.connect(SensibleGlobal.URL+"/user_login")
                    .method(Method.POST)
                    .requestBody(json.toJSONString())
                    .header("Accept", "application/json")
                    .header("Content-Type", "application/json")
                    .ignoreContentType(true).post();
            JSONObject object = (JSONObject) new JSONParser().parse(document.text());
            String token = object.get("message").toString();
            SensibleGlobal.token = token;
            java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                    CRM crm = new CRM();
                    crm.setLocationRelativeTo(null);
                    crm.setVisible(true);
                }
            });
        } 
        catch (IOException ex) 
        {
            Logger.getLogger(RestLogin.class.getName()).log(Level.SEVERE, null, ex);
        } catch (ParseException ex) {
            Logger.getLogger(RestLogin.class.getName()).log(Level.SEVERE, null, ex);
        }
        status.setText("LOGIN");
    }

}
