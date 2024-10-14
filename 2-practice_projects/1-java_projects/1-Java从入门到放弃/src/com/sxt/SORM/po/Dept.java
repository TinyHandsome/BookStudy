package com.sxt.SORM.po;

import java.sql.*;
import java.util.*;

public class Dept {

	private String address;
	private Integer id;
	private String dname;


	public void setAddress(String address){
		this.address = address;
	}
	public void setId(Integer id){
		this.id = id;
	}
	public void setDname(String dname){
		this.dname = dname;
	}
	public String getAddress(){
		return address;
	}
	public Integer getId(){
		return id;
	}
	public String getDname(){
		return dname;
	}
}
